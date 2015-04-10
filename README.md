Weather•Ma•Jig
===

##It's a thing-a-ma-jig for weather&hellip;and the command line

insired by this thread on reddit: http://www.reddit.com/r/commandline/comments/1jjgu1/bash_getting_weather/

Instructions:
---
* get a [forcast.io](https://developer.forecast.io/) api key
* clone this directory
* ensure you have python2 and pip setup
* use pip to install requirements.txt

```
sudo pip -r requirements.txt
```

* install this thing

```
sudo python2 setup.py install
```

* Create a `~/.weathermajig` yaml config file like

```yaml
---
# Dark sky api key
api_key: 123456789notakey
cache_dir: /tmp/weathermajig.cache
```

* enjoy the weather

```
$ weathermajig "Boulder"
☁ Mostly Clo… [47°F]

$ weathermajig -v "Boulder"

Thu 04/09/15 07:40:34 PM
Forecast for Boulder
---
CURRENTLY: 47.1°F
HIGH: 54.75°F
LOW: 36.54°F
☁ Mostly Cloudy

```

Screenshot:
---

Here's what this looks like running on a non-mac:

<img src="20130804_p_weather.png" title="Weather-ma-jig at work" />

Sweet Emoji on Mac!

<img src="20130904_p_weather_on_darwin.png" title="Weather-ma-jig at work on OSX" />