#Have the user enter the cost of the loan, the interest rate,
#the number of years for the loan
#Calculate monthly payments with the following formula:
# M = L[i(1+i)n] / [(1+i)n - 1]
# M = monthly payment
# L = loan amount
# i = interest rate ( for an interest rate of 5%, i = 0.05)
# n = number of payments
#_____________________________________________________________
#Start of Program
#Declare variables

monthlyPayment = 0
loanAmount = 0
numberOfYears = 0
interestRate = 0
numberOfPayments = 0

strLoanAmount = input("Enter the loan amount: ")
strInterestRate = input("Enter the interest rate: ")
strNumberOfYears = input("Enter the number of years: ")

#Convert the strings into float numbers so we can use them in the formula

loanAmount = float(strLoanAmount)
interestRate = float(strInterestRate)/12
numberOfYears = float(strNumberOfYears)

#Since payments are one per month, there are 12 payments in a year]

numberOfPayments = numberOfYears * 12

#Calculate the monthly payment based on the formula

monthlyPayment = loanAmount * interestRate * (1 + interestRate) ** numberOfPayments / \
    (1 + interestRate) ** numberOfPayments - 1

print("Your monthly payment on the loan will be: {0:.2f}" .format(monthlyPayment))
