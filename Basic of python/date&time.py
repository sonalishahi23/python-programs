import datetime    #current date time
date_time=datetime.datetime.now()
print("Current Date & Time: ",date_time)

future_date=date_time + datetime.timedelta(days=10) #after 10 days date time
print("After 10 Days Date & Time will be : ",future_date)

past_date=date_time + datetime.timedelta(days=-10) #before 10 days date time
print("Before 10 Days Date & Time was : ",past_date)

current_date=date_time.strftime("%Y/%m/%d")# Current date only
print("Current date is ",current_date)

current_time=date_time.strftime("%H:%M:%S")#current time only
print("Current Time is ",current_time)

import time  # sleeping os for some seconds

data=[10,20,30,40,50]  
print("Searching.....")
time.sleep(5)
for i in data:
    time.sleep(3)
    print(i)

import calendar
year2026=calendar.calendar(2026)
print(year2026)

feb=calendar.month(2026,2)
print(feb)

