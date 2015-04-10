#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from weathermajig import config
from weathermajig import geo
from weathermajig import weather
from weathermajig import cache
from weathermajig import output

def main():
    conf = config.Config()
    cache.check(conf)
    lat, lng = geo.get_loc(conf)
    api_key = conf.get('api_key')

    wthr = weather.Weather(api_key=api_key, lat=lat, lng=lng)
    output.make(conf, wthr)

if __name__ == '__main__':
    main()