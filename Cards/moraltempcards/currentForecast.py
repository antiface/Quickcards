import urllib
import simplejson
 
# Replace /APIKEY/LATITUDE,LONGITUDE with appropriate information.
 
request = urllib.urlopen('https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE')
forecastData = simplejson.loads(request.read())

currentTemp = forecastData['currently']
