balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterest = annualInterestRate/12
for i in range(12):
    minMonthPay = monthlyPaymentRate*balance
    monthlyUnpaidBal = balance - minMonthPay
    balance = monthlyUnpaidBal + (monthlyInterest*monthlyUnpaidBal)
print('Remaining balance: ' + str(round(balance, 2)))

