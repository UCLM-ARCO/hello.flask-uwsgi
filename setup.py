#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

from setuptools import setup


setup(name='hello',
    version      = '0.0.1',
    description  = 'uWSGI flask minimal example',
    author       = 'David Villa Alises',
    author_email = 'David.Villa@gmail.com',
    packages     = ['hello'],
    install_requires = [
        'Flask>1.0.0',
    ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    data_files=[
        ('/etc/uwsgi/apps-available',    ['uwsgi/hello.ini']),
        ('/etc/nginx/sites-available',   ['nginx/hello']),
    ],
)
