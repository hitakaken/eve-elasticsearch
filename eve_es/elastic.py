# -*- coding: utf-8 -*-

import elasticsearch
import logging


import eve_elastic.elastic as elastic
from eve_elastic import Elastic as Base
from eve.utils import config, str_type

logger = logging.getLogger('elastic')


class Elastic(Base):
    def __init__(self, app, **kwargs):
        self.kwargs = kwargs
        super(Elastic, self).__init__(app)

    def put_mapping(self, app, index=None):
        """Put mapping for elasticsearch for current schema.

        It's not called automatically now, but rather left for user to call it whenever it makes sense.
        """

        for resource, resource_config in app.config['DOMAIN'].items():
            datasource = resource_config.get('datasource', {})

            if not elastic.is_elastic(datasource):
                continue

            if datasource.get('source', resource) != resource:  # only put mapping for core types
                continue

            properties = self._get_mapping(resource_config['schema'])
            properties['properties'].update({
                config.DATE_CREATED: self._get_field_mapping({'type': 'datetime'}),
                config.LAST_UPDATED: self._get_field_mapping({'type': 'datetime'}),
            })

            kwargs = {
                'index': index or self.index,
                'doc_type': resource,
                'body': properties,
                # 'ignore_conflicts': True,
            }

            try:
                self.es.indices.put_mapping(**kwargs)
            except elasticsearch.exceptions.RequestError:
                logger.warning('mapping error, updating settings resource=%s' % resource)
                self.put_settings(app, index)
                self.es.indices.put_mapping(**kwargs)
