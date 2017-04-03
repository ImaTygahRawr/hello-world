# You can perform math operations on numeric values
# or on variables containing numeric values

#width = 20
#height = 5
#area = width * height
#print(area)

#perimeter = 2*width + 2*height
#perimeter = 2*(width + height)
#print(perimeter)

#Most common math operators/ PEMDAS order of operations still apply.
#Addition: 5 + 2 = 7
#Subtraction: 5-2 = 3
#Multiplication: 5*2 = 2.5
#Division: 5/2 = 2.5
#Exponent: 5**2 = 25
#Modulo: 5%2 = 1

area = 0
height = 10
width = 20
#calculate area of a triangle
area = width * height /2

print(area)

#Sometimes you will need to format the numbers when you
#display them to users

print("I have %d cats" % 6) # %d simply means a digit, or whole number
print("I have %3d cats" % 6) # %3d simply means number is adjusted 3 spaces right
print("I have %03d cats" % 6) # %03d means 3 digits long with zeroes inserted
print("I have %f cats" % 6) # %f simply means float number, with decimals
print("I have %.2f cats" % 6) # .2f determines how many decimal places to display

print("the area of the triangle would be %.2f" % area)

print("My favorite number is %d" % 23)

# You can also use a format method to format numeric values

print("I have {0:d} cats".format(6)) # %d simply means a digit, or whole number
print("I have {0:3d} cats".format(6)) # %3d simply means number is adjusted 3 spaces right
print("I have {0:03d} cats".format(6)) # %03d means 3 digits long with zeroes inserted
print("I have {0:f} cats".format(6)) # %f simply means float number, with decimals
print("I have {0:.2f} cats".format(6)) # .2f determines how many decimal places to display


#Do the same thing with the .format syntax to include numbers in output
#If a line of code is too long, use a \ "backslash" to move rest to next line
print("the area of the triangle would be {0:f}" .format(area))
print("my favorite number is {0:d}" .format(42))
print("Here are three numbers! this is {0:d},\
the second is {1:4d}, and {2:d}" .format(5,4,3))

