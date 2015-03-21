#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
from time import time

def get_cache(conf):
    # unique key for caching
    conf.get_key()
    return yaml.load(file(self._config_loc, 'r'))

def get_dir(conf):
    cache_dir = conf.get('cache_dir')
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    return cache_dir

def get_file(conf):
    cache_file = os.path.join(get_dir(conf), conf.get_key())

    return cache_file

def check(conf):
    now = time()
    ten_minutes_ago = now - 60 * 10
    file = get_file(conf)
    if (os.path.exists(file)):
        file_last_modified = os.path.getmtime(file)
        if (file_last_modified > ten_minutes_ago):
            cache = open(file, 'r')
            print cache.read()
            sys.exit(0)

def write(conf, content):
    file = get_file(conf)
    dir = os.path.dirname(file)
    if not os.path.exists(dir):
        os.makedirs(dir)
    cache = open(file, 'w')
    cache.write(content)

