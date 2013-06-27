import urllib
import simplejson
 
# Replace /APIKEY/LATITUDE,LONGITUDE with appropriate information + add query parameter ?unit=ca to get units in Canadian format.
 
request = urllib.urlopen('https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE')
forecastData = simplejson.loads(request.read())

currentTemp = forecastData['currently']
