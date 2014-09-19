import os
import requests
import json
 
os.chdir('C:\\Users\etc')
r = requests.get('https://api.forecast.io/forecast/APIKEY/45.5599,-73.1856')
 
import json
 
with open('currently.txt', 'a') as outfile:
	json.dump(r.json()['currently'], outfile)
 
current = {'time': currently['time'], 'temperature': currently['temperature'],
'humidity': currently['humidity'], 'pressure': currently['pressure'], 'windSpeed': currently['windSpeed']}
 
"""
current
{'pressure': 1012.82, 'windSpeed': 8.59, 'humidity': 0.67, 'temperature': 69.03, 'time': 1401063717}
 
with open('currently.txt', 'a') as outfile:
	json.dump(current, outfile)
 
>>> type(r.json())
<type 'dict'>
>>> r.json().keys()
[u'hourly', u'currently', u'longitude', u'flags', u'daily', u'offset', u'latitude', u'timezone', u'minutely']
 
>>> r.json()['currently']
{u'ozone': 364.78, u'temperature': 71.38, u'dewPoint': 58.23, u'precipType':
u'rain', u'nearestStormDistance': 0, u'precipIntensityError': 0.0017, u'humidity': 0.63,
u'visibility': 9.99, u'summary': u'Light Rain', u'apparentTemperature': 71.38, u'pressure': 1012.83,
u'windSpeed': 9.53, u'precipProbability': 1, u'cloudCover': 0.98, u'time': 1401062920,
u'windBearing': 231, u'precipIntensity': 0.0222, u'icon': u'rain'}
 
"""
