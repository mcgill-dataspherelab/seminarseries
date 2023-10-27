def min_mth_pay(balance, monthlyPaymentRate):
    x = balance * monthlyPaymentRate
    return x

def balance(balance, min_mth_pay, annualInterestRate):
    y = (balance - min_mth_pay) * ((annualInterestRate / 12) + 1)
    return y

print("Hello DataSphereLab")

test=0
test=1
test0=0
test1=1
test2=2

#Don't print your variables anymore, use the debugger
print(f"Here is my variable test0: {test0}")
print(f"Here is my variable test1: {test1}")
print(f"Here is my variable test2: {test2}")


balance = float(input("Enter the outstanding balance on your credit card: "))
annualInterestRate = float(input("Enter the annual credit card interest rate as a decimal: "))
monthlyPaymentRate = float(input("Enter the minimum monthly payment rate as a decimal: "))

a = 0
while a <= 11:
    a += 1
    x = min_mth_pay(balance, monthlyPaymentRate)
    y = balance(balance, x, annualInterestRate)
    print("Month:", a)
    print("Minimum monthly payment:", round(x, 2))
    print("Remaining balance:", round(y, 2))
    balance = y