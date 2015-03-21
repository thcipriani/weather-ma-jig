#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from geopy.geocoders import Nominatim

def get_lat(place):
    geoloc = Nominatim()
    lat_long = geoloc.geocode(place)
    return (lat_long.latitude, lat_long.longitude)
