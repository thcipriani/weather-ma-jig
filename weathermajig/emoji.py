#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

def get_emoji():
    platform = sys.platform
    if platform.startswith('linux'):
        return {
            'sun': "☀",
            'snow': "❄",
            'rain': "☂",
            'cloud': "☁",
            'default': "✔",
        }

    if platform.startswith('darwin'):
        return {
            sun: "🌞 ",
            snow: "❄️ ",
            rain: "☔ ",
            cloud: "⛅ ",
            default: "🌏 ",
        }

def icon(conditions):
    emoji = get_emoji()
    cond = conditions.lower()

    if 'cloud' in cond:
        return emoji.get('cloud')

    if 'snow' in cond or 'sleet' in cond or 'hail' in cond:
        return emoji.get('snow')

    if 'rain' in cond or 'storm' in cond:
        return emoji.get('rain')

    if 'clear' in cond or 'sun' in cond:
        return emoji.get('sun')

    return emoji.get('default')

