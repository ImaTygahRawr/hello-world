
#This is a comment which is used to explain the following lines of code
print("There once was a movie star icon")
print("Who prefered to sleep with the light on.")
print("They learned how to code \na device that sure glowed \nand lit up the night using Python!\n")

#Tiny user input generated program
#You can combine variables and strings with the + symbol :D
name = ""
name = input("Please enter your name: ")
import string
name = string.capwords(name)
print(name)


country = input("What country do you live in, " + name + "?: ")

#manipulating the casing of the country variable
country = string.capwords(country)
print("Welcome, " + name + " from " + country + "!")

#Creating a friendly output
print("Hello and welcome to my first program, " + name + "!\n")

#name = ("Daniel")
#print(name)

#camelCasing is lowercase first v.s. PascalCasing which is upper case first
favoriteSign = ""
favoriteSign = input("What is your zodiac sign?")
favoriteSign = favoriteSign.capitalize()
print("Thank you for answering, " + favoriteSign + "!\n")

#Variables also allow you to manipulate the contents of the variable
message = "Hello World"
print(message.lower())
print(message.upper())
print(message.swapcase())

#Practicing functions - What do you think these will do?
message = "what's up, bruh? \n"
print(message.find("up"))
print(message.count("u"))
print(message.capitalize())
print(message.replace("what's up", "How are you on this fine evening"))

#Sometimes, IntelliSense won't appear to help like wen trying to use the upper() function
#That's because the program doesn't know a string value is going to be stored in the postalCode variable.
#The upper() function is only for strings. A good habit when coding in any language is to initialize
#your variables with an initial value.

postalCode = ""
postalCode = input("Please enter your Postal Code:")
print(postalCode.upper())

