# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

install_requires = [
    'eve>=0.6.0',
    'elasticsearch>=2.0.0,<3.0',
    'eve-elastic>=0.3.8',
]

setup(
    name='Eve-ElasticSearch',
    version='0.0.2',
    description='Elasticsearch data layer for eve rest framework and elasticsearch 2.x',
    long_description=readme,
    author='CaoKe',
    author_email='hitakaken@gmail.com',
    url='https://github.com/hitakaken/eve-elasticsearch',
    license=license,
    platforms=["any"],
    packages=['eve_es'],
    test_suite="test.tests",
    install_requires=install_requires,
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    data_files=[('', ['README.md', 'LICENSE'])]
)