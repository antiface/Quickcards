import time
import urllib
import simplejson
from mongoengine import *

connect('moraltempcards')

class Temp(Document):
    temp = DictField()

class Time(Document):
    time = StringField()

class Note(Document):
    content = StringField()
    time = ReferenceField(Time)
    temp = ReferenceField(Temp)

currentTime = time.asctime()
currentTime = Time(time=currentTime)
currentTime.save()

# Replace /APIKEY/LATITUDE,LONGITUDE with appropriate information + add query parameter ?unit=ca to get units in Canadian format.
 
request = urllib.urlopen('https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE')
forecastData = simplejson.loads(request.read())

currentTemp = forecastData['currently']
currentTemp = Temp(temp=currentTemp)
currentTemp.save()
 
newNote = ''
 
def inputText():
    text = {}
    askVar = raw_input("Type note: ")
    text = askVar
    return text
 
newNote = inputText()

note = Note(content=newNote)
note.time = currentTime
note.temp = currentTemp
note.save()
