# Greeting message
print("Welcome, this is your consumption bill until the end of the month!" )
# Here you write your current account balance
bank = input("Your current account balance? $")
# Here you add the minimum amount that must always remain in the account
minimum = input("How much minimum do you leave on the account? $")
# Here you enter the number of days until the next payment
payment_day = input("How many days until the next payment?")
# Now we do the math part of the equation
a = float(bank)
b = float(minimum)
c = int(payment_day)
d = ((a-b)/c)
# Finally! How much should you spend every day in order not to exceed the minimum figure!
print(f"The maximum daily consumption is:: ${d}")