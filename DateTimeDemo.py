import datetime

dateTime = datetime.datetime.now()
print("Current Time:",dateTime)

dateTime = datetime.datetime.utcnow()
print("UTC Time: ",dateTime)

print("Complete Year:",dateTime.strftime('%Y'))
print("Last 2 digit of Year:",dateTime.strftime('%y'))

print("My Own Format: ",dateTime.strftime('%y/%m/%dT%H:%M:%S'))
print("Just Time: ",dateTime.strftime('%H:%M:%S'))

from datetime import date

print(date.today())
print(date.strftime('%y/%m/%d'))