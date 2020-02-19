#We use a library


# How to change reference
#   from datetime import datetime as dt
#   currentDay= dt.now()
#   print ("Today is " + str(currentDay))


#   How ro import several directories from the same library

from datetime import datetime, timedelta

today= datetime.now()
print ("Today is " + str(today))
twoDays = timedelta(2)
dayBeforeYesterday = today-twoDays
print("The day before yesterday was " + str(dayBeforeYesterday))

#Ok, so.. timedelta, we can use the following methods:

twoDays = timedelta(2) #By default, these are days
#But we can change it
twoDays = timedelta(days=2)
day = today-twoDays
print("The day before yesterday was " + str(day))

# twoDays = timedelta(month=2)
# day = today-twoDays
# print("Two months ago was " + str(day))

twoDays = timedelta(weeks=2)
day = today-twoDays
print("Two weeks ago was " + str(day))

# twoDays = timedelta(years=2)
# day = today-twoDays
# print("Two years was " + str(day))