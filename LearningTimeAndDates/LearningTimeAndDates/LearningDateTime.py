#If I want to know how many days until my birthday, first I need today's date

#The datetime class allows us to get the current date and time

#The import statement gives us access to
#the functionality of the datetime class

import datetime

#today is a function that returns today's date


currentDate = datetime.date.today()

print(currentDate)

# You can access different parts of the date

print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

#What date does 12/06/09 represent?

#What if you want to display the date with a specific format?

#Different countries and different users like different date formats,
#often the default isn't what you need

#There is always a way to handle it, but it will take a little time and extra code

#strftime allows you to specify the date format
# %b: month abbreviated
# %B: full month name
# %Y: full year
# %y: 2 digit year
# %a: day of week abbreviated
# %A: day of week
# Full list at strftime.org

print (currentDate.strftime("%a %b %d, %Y"))

# Could you print out a wedding invitation?

print(currentDate.strftime
("Please attend our event on the evening of %A the 3rd, month of %B, in the year %Y"))

#What if I don't want English? 
#In programmer speach we call that Localization
#By default the program uses the language of the machine it's running on
#But... since you can't always realy on PC settings it is possible to force
#Python to use a particular language.
#It just takes more time and more code. If you need to do that, check out
#the babel Python library at http://babel.pocoo.org/

birthday = input("What is your birthday?")
print("Your birthday is " + birthday)

#How do we convert input from a string into a date?

birthdate =  datetime.datetime.strptime(birthday, "%m/%d/%Y")

#Why did we list datetime twice?
#Because we are calling the strptime function
#which is part of the datetime class
#which is in the datetime module

print("Your birth month is " + birthdate.strftime("%B"))

import datetime

currentDate = datetime.date.today()

userInput = input("Please enter your birthday: ")
birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y")
print(birthday)

#But what if the user doesn't enter the date in the format I specify in strptime?
#Your code will crash so...
#Tell the user the date format you want

birthday = input("What is your bithday? (mm/dd/yyyy)")
print(birthday)

#You can also add Error Handling