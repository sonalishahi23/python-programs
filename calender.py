import calendar
year=int(input("please Enter the year you want to see the calender: "))
month=int(input("please Enter the month you want to see: "))
display=calendar.month(year,month)
print(display)