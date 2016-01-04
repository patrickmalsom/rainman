#!/usr/bin/env python3.4

# API key from openweathermap
api_key = ''

# Latitude and Longitude to set your position
latitude=42.3
longitude=-85.6

# Cache timeouts 
#    (free OWM account has restrictions on number of downloads/hr)
cache_forecast_expire = 7200 # redownload cache at 2 hrs
cache_weather_expire = 600   # redownload cache at 10 mins

# location of downloaded weather file for cache
weather_file_name = '/tmp/.weather_weather'
forecast_file_name = '/tmp/.weather_forecast'
