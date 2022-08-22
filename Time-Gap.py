# Time Gap

# Importing datetime module

import datetime, time

# Asking and reading the date of the event, event name from the user

name_of_event= str(input("Enter the event name     "))
name_of_event= name_of_event.capitalize()
year_of_event= int(input("Please enter the year of your event. For e.g. 2000-2100     "))
month_of_event= int(input("Please enter the month of your event. For e.g. 01-12     "))
day_of_event= int(input("Please enter the day of your event. For e.g. 1-31     "))


"""
Calculating the number of seconds of the date since origin (The epoch), obtaining the current
time instant and calculating the difference between two dates. 
"""

# Initial time/ the current time instant taken as t1 and the time of event or future time as t2

t= datetime.datetime(year_of_event, month_of_event, day_of_event,0,0)
t1= time.mktime(t.timetuple())
t2= time.time()
diff= t1-t2

# Converting the time differences(Seconds) into Year, Day, Hour, Minutes and seconds.

year= int(diff//(365*24*60*60))
diff= diff%(365*24*60*60)
day= int(diff//(24*60*60))
diff= diff%(24*60*60)
hour= int(diff//(60*60))
diff= diff%(60*60)
mins= int(diff//60)
diff= diff%60
sec= int(diff)

print(f'\"{name_of_event} is on {day_of_event}/{month_of_event}/{year_of_event}'
      f'({year} years, {day} days, {hour} hours,'
      f' {mins} minutes and {sec} seconds later).\"')
