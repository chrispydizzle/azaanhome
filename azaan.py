import json
import urllib2
import datetime
import time
from datetime import timedelta
from playsound import playsound


def parse_time(collection, value):
    the_time = datetime.datetime.strptime(collection[value], '%I:%M %p').replace(theTime.year, theTime.month,
                                                                                 theTime.day)
    print '%s, %s' % (value, the_time)
    return the_time


def check_time(first_call, current_time):
    if current_time < datetime.datetime.now():
        print 'fajr'
        if not first_call:
            playsound('azaan.wav')
        return current_time.replace(year=datetime.MAXYEAR)
    return current_time


if __name__ == '__main__':
    while True:
        print 'new cycle!'
        print datetime.datetime.now()
        theTime = datetime.datetime.now()
        secret = open("top_secret.txt")
        my_secret = secret.read()
        urlopener = urllib2.build_opener()
        urlopener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        times = urlopener.open('http://muslimsalat.com/newyork.json?key=' + my_secret)
        posts = json.loads(times.read())
        items = posts['items'][0]
        dateFor = datetime.datetime.strptime(items['date_for'], '%Y-%m-%d')
        fajrTime = parse_time(items, 'fajr')
        shrooqTime = parse_time(items, 'shurooq')
        dhuhrTime = parse_time(items, 'dhuhr')
        asrTime = parse_time(items, 'asr')
        maghribTime = parse_time(items, 'maghrib')
        ishaTime = parse_time(items, 'isha')
        first_time = True
        loops = 0
        while datetime.datetime.now() < (dateFor + timedelta(days=1)):
            loops += 1
            if loops > 15:
                loops = 0
                print 'fifteen minute check-in'

            theTime = datetime.datetime.now()
            fajrTime = check_time(first_time, fajrTime)
            # shrooqTime = check_time(first_time, shrooqTime)
            dhuhrTime = check_time(first_time, dhuhrTime)
            asrTime = check_time(first_time, asrTime)
            maghribTime = check_time(first_time, maghribTime)
            ishaTime = check_time(first_time, ishaTime)

            first_time = False
            time.sleep(60)
