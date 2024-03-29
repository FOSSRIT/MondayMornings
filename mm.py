#import statements
#wunderground libs
import urllib2
import json
import pygame
import datetime
import random
from time import sleep

#Alarm functionality
#--------------------------------------------------------------------------
#inits()
pygame.init()
# get the alarm sound ready to go
pygame.mixer.music.load('missle_alarm.wav')

# returns seconds to wait to start alarm
def howlong(alarmtime):
    now = datetime.datetime.now() # get current date & time
    
    # separate date and time from each other:
    currdate = datetime.date(getattr(now, "year"), getattr(now,"month"), getattr(now,"day")) 
    currtime = datetime.time(getattr(now, "hour"), getattr(now, "minute")) 
    
    # convert user entered time into python time format
    alarmtime = datetime.datetime.strptime(alarmtime, '%I:%M')
    alarmtime = datetime.time(getattr(alarmtime, "hour"), getattr(alarmtime, "minute"))
    # add today's date onto the alarm time entered
    alarmdatetime = datetime.datetime.combine(currdate, alarmtime)
    
    if alarmtime < currtime: # if the alarm time is less than the current time set clock for tomorrow
        alarmdatetime += datetime.timedelta(hours=12)
    
    return alarmdatetime - now

def mathprob(num1, num2, userans): # see if i've solved the problem
    return int(userans) == num1 + num2
    
usertime = raw_input("Enter the time you want [hh:mm] > ")
z = howlong(usertime)
sleep(z.seconds) # wait until it is time for the alarm to go off

pygame.mixer.music.play() # start the alarm 

random.seed()
num1 = random.randrange(100, 999) # generate two numbers at random to test for addition
num2 = random.randrange(100, 999)

puzzle = raw_input("Good morning.  To stop the alarm, add these numbers: %r + %r > " % (num1, num2))
solved = mathprob(num1, num2, puzzle)

while solved == False:
    puzzle = raw_input("That is not right.  Try again.  %r + %r -> " % (num1, num2))
    solved = mathprob(num1, num2, puzzle)

pygame.mixer.music.stop()

print "Good Maths. Time to GAUX!"

#Weather functionality - courtesy of the weather underground API
#--------------------------------------------------------------------------
f = urllib2.urlopen('http://api.wunderground.com/api/______Your API Key______/geolookup/conditions/q/IA/Rochester.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
windchill = parsed_json['current_observation']['windchill_f']
weather = parsed_json['current_observation']['weather']
print "Current weather in %s is %s at a temperature of: %s degrees, with a windchill of %s degrees" % (weather,location, temp_f, windchill)
f.close()




