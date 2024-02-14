# bank.py
# Author: Matthias Wiedemann

# I created three variables to get to the desired outcome 

a = int(input("Enter 1st amount in cent: "))
b = int(input("Enter 2nd amount in cent: "))
c = (a + b) / 100

# Result printed by using 'f' function:

print(f"The sum is: {c} €")

# Result printed by using 'str' function:

print("The sum is: " + str(c) + " €")

