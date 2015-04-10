#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import argparse
import yaml

class ConfigException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Config:
    def __init__(self):
        self._args= self._parse_args()
        self._config_loc = self.get(
            'config',
            os.path.join(os.getenv('HOME'), '.weathermajig')
        )
        self._config = self._parse_config()
        self._args = dict(self._args.items() + self._config.items())

    def _parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('place',
                help='location, e.g. 80501 or "Boulder, CO"')
        parser.add_argument('-v', '--verbose',
                help='more verbose output',
                action='store_true')
        parser.add_argument('-c', '--config',
                help='override default config location (~/.weathermajig)')
        return vars(parser.parse_args())

    def _parse_config(self):
        if not os.path.exists(self._config_loc):
            raise ConfigException('{} not found'.format(self._config_loc))
        return yaml.load(file(self._config_loc, 'r'))

    def get_key(self):
        return '_'.join(['%s-%s' % (k, v) for (k, v) in self._args.iteritems() if k != 'api_key'])

    def get(self, key, default=None):
        val = self._args.get(key)
        if not val:
            return default

        return val
