import json
import urllib2
import datetime
import time
from datetime import timedelta
from playsound import playsound

if __name__ == '__main__':
    while True:
        print 'new cycle!'
        print datetime.datetime.now()
        theTime = datetime.datetime.now()
        secret = open("top_secret.txt")
        my_secret = secret.read()
        times = urllib2.urlopen('http://muslimsalat.com/newyork.json?key=' + my_secret)
        posts = json.loads(times.read())
        items = posts['items'][0]
        dateFor = datetime.datetime.strptime(items['date_for'], '%Y-%m-%d')
        fajrTime = datetime.datetime.strptime(items['shurooq'], '%H:%M %p').replace(theTime.year, theTime.month,
                                                                                    theTime.day)
        dhuhrTime = datetime.datetime.strptime(items['dhuhr'], '%H:%M %p').replace(theTime.year, theTime.month,
                                                                                   theTime.day)

        dhuhrTime = dhuhrTime.replace(hour=dhuhrTime.hour + 12)

        asrTime = datetime.datetime.strptime(items['asr'], '%H:%M %p').replace(theTime.year, theTime.month, theTime.day)
        asrTime = asrTime.replace(hour=asrTime.hour + 12)
        maghribTime = datetime.datetime.strptime(items['maghrib'], '%H:%M %p').replace(theTime.year, theTime.month,
                                                                                       theTime.day)
        maghribTime = maghribTime.replace(hour=maghribTime.hour + 12)
        ishaTime = datetime.datetime.strptime(items['isha'], '%H:%M %p').replace(theTime.year, theTime.month,
                                                                                 theTime.day)
        ishaTime = ishaTime.replace(hour=ishaTime.hour + 12)
        first_time = True
        loops = 0
        while datetime.datetime.now() < (dateFor + timedelta(days=1)):
            loops += 1
            if loops > 15:
                loops = 0
                print 'fifteen minute check-in'

            theTime = datetime.datetime.now()
            if fajrTime < theTime:
                print 'fajr'
                if not first_time:
                    playsound('azaan.wav')
                fajrTime = fajrTime.replace(year=datetime.MAXYEAR)
            if dhuhrTime < theTime:
                print 'dhuhr'
                if not first_time:
                    playsound('azaan.wav')
                dhuhrTime = dhuhrTime.replace(year=datetime.MAXYEAR)
            if asrTime < theTime:
                print 'asr'
                if not first_time:
                    playsound('azaan.wav')
                asrTime = asrTime.replace(year=datetime.MAXYEAR)
            if maghribTime < theTime:
                print 'maghrib'
                if not first_time:
                    playsound('azaan.wav')
                maghribTime = maghribTime.replace(year=datetime.MAXYEAR)
            if ishaTime < theTime:
                print 'isha'
                if not first_time:
                    playsound('azaan.wav')
                ishaTime = ishaTime.replace(year=datetime.MAXYEAR)
            first_time = False
            time.sleep(60)
