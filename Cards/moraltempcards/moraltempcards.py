import time
import urllib
import simplejson
import pymongo
from pymongo import Connection
 
connection = Connection()
db = connection.moraltempcards
db.moraltempcards
 
currentTime = time.asctime()
 
# Replace /APIKEY/LATITUDE,LONGITUDE with appropriate information + add query parameter ?unit=ca to get units in Canadian format.
 
request = urllib.urlopen('https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE')
forecastData = simplejson.loads(request.read())
 
currentData = forecastData['currently']
 
newNote = ''
 
def inputText():
  text = {}
	askVar = raw_input("Type note: ")
	text['date'] = currentTime
	text['note'] = askVar
	text['currentTemp'] = currentData
	return text
 
newNote = inputText()
 
db.moraltempcards.save(newNote)
