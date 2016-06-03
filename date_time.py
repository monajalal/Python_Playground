#working with datetime python lib
import datetime

print(dir(datetime))
print(datetime.datetime.now())
start_time = datetime.datetime.now()
end_time = datetime.datetime.now()

print(end_time-start_time)
new_time = start_time.replace(hour=9, second =15)
another_time = datetime.datetime(1987,7,23,7,30)
print(another_time)
print(new_time)
diff =start_time - another_time
print(diff)

print()

print(datetime.datetime.now())
print(datetime.datetime.now() - datetime.timedelta(minutes=15))
print(datetime.datetime.now() + datetime.timedelta(minutes=-15))
print(datetime.timedelta(hours=5))
print(datetime.datetime.now()+datetime.timedelta(days = 3))
#go back in time
print(datetime.datetime.now()+datetime.timedelta(days=-9))
#or go back in time more fashionably
print(datetime.datetime.now()-datetime.timedelta(days=9))


#get the time
print(datetime.datetime.now().date())
#get the date
print(datetime.datetime.now().time())
print()
print(datetime.datetime.combine(datetime.datetime.today(), datetime.time()))
today = datetime.datetime.today()
weekday = today.weekday()
print(weekday)
print(datetime.datetime.now().timestamp())

def minutes(datetime1, datetime2):
    seconds = (datetime1 - datetime2).timedelta.total_seconds()
    return round(seconds/60)

print(datetime.datetime.now().strftime('%B/%d/%Y'))

print(datetime.datetime.strptime('1987-7-23', '%Y-%m-%d'))

birthday_party = datetime.datetime.strptime('07/23/2016 18:00', '%m/%d/%Y %H:%M')

"""


Hope you find this useful:

    from datetime import datetime
    datetime_object = datetime.datetime.strptime('Fri, 03 Jun 2016 08:01:26 GMT'
                                                 , '%a, %d %b %Y %H:%M:%S %Z')
    print(datetime_object)

In above we have:

`%a` : abbreviated weekday name

`%d` : numerical day

`%b` : abbreviated month name

`%Y` : century-based years

`%H` : hour (24 hour based)

`%M` : minutes

`%S` : seconds

`%Z` : timezone

Have a look at other formats [here][1].


  [1]: http://www.tutorialspoint.com/python/time_strptime.htm



"""

datetime_object = datetime.datetime.strptime('Fri, 03 Jun 2016 08:01:26 GMT',
                                             '%a, %d %b %Y %H:%M:%S %Z')
print(datetime_object)
print(birthday_party)

def time_tango(date, time):
    return datetime.datetime.combine(date, time)

def to_string(datetime):
    return datetime.datetime.strptime('24 09 2012', '%d %m %Y')
