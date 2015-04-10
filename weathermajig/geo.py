#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from geopy.geocoders import Nominatim

def get_loc(conf):
    lat = conf.get('lat')
    lng = conf.get('lng')

    if lat is None or lng is None:
        geoloc = Nominatim()
        lat_long = geoloc.geocode(conf.get('place'), timeout=10)
        lat = lat_long.latitude
        lng = lat_long.longitude

    return (lat, lng)
