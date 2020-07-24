balance = 4773
annualInterestRate = 0.2

monthlyInterest = annualInterestRate/12
lowestPayment = 0
newBalance = balance

while newBalance > 0:
    lowestPayment += 10
    newBalance = balance
    month = 1

    while month <= 12 and newBalance > 0:
        newBalance -= lowestPayment
        interest = monthlyInterest*newBalance
        newBalance += interest
        month +=1
    newBalance = round(newBalance,2)

print('Lowest payment: ' + str(round(lowestPayment, 2)))
