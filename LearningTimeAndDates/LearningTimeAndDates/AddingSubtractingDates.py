##Dates seem like a lot of hassle. Is it worth it?
##Why not just store them as strings?!
##You can create a countdown to say how many days until a big event or holiday

import datetime

#nextBirthday = \
#    datetime.datetime.strptime("12/20/2017","%m/%d/%Y").date()

currentDate = datetime.date.today()

##If you subtract two dates you get back the number of days
##between those two dates

#difference = nextBirthday - currentDate
#print(difference.days)

userInput = input("Please enter your birthday (mm/dd/yyyy) ")
birthday = datetime.datetime.strptime(userInput,"%m/%d/%Y").date()
print(birthday)

days = birthday - currentDate
print(days.days)

#You'll be amazed how often you need to work with dates!
#If datetime doesn't have what you need, check out the dateutil
#library (for example you might want to know the number of years
#between two dates instead of number of days

