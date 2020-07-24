balance = 999999
annualInterest = .18

monthlyInterest = annualInterest / 12.0
lowerbound = balance / 12
upperbound = (balance*(1+monthlyInterest)**12)/12.0
epsilon = 0.01

newBalance = balance
while abs(newBalance) > epsilon:
    lowestPayment = (lowerbound + upperbound)/2
    newBalance = balance
    month = 1

    while month <=12:
        newBalance -= lowestPayment
        interest = monthlyInterest*newBalance
        newBalance += interest
        month +=1
    if newBalance > epsilon:
        lowerbound = lowestPayment
    elif newBalance < epsilon:
        upperbound = lowestPayment

print('Lowest payment: ', round(lowestPayment, 2))