#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests as req

class Weather:
    DARK_SKY_URL = 'https://api.forecast.io'

    def __init__(self, lat=None, lng=None, api_key=None):
        self._lat, self._long, self._key  = (lat, lng, api_key)
        self.get_weather()

    def __getattr__(self, attr):
        return self._forecast.get(attr)

    def get_weather(self):
        url = "%s/forecast/%s/%s,%s" % (Weather.DARK_SKY_URL, self._key, self._lat, self._long)
        self._forecast = req.get(url).json()
        return self

    def get_current(self):
        return self._forecast.get('currently')

    def get_today(self):
        return self._forecast.get('daily').get('data')[0]
