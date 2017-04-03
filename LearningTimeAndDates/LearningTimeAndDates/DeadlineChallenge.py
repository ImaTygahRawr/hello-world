# Ask a user to enter the deadline for their project
# Tell them how many days they have to complete the project
#For extra credit, give them the answer as a combination of weeks
#and days (Hint: you'll need math functions from numeric values module)


import datetime

userDeadline = input("Enter a deadline for your project (mm/dd/yyyy): ")

currentDate = datetime.datetime.today()

deadLine = datetime.datetime.strptime(userDeadline, "%m/%d/%Y").date()

daysLeft = deadLine - currentDate

print("You have " + daysLeft.strftime("%d") + "until the deadline of your project.")
