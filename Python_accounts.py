# Python accounts
# Author: Matthias Wiedemann

# Created variable for account number using input (as it is a prompt) & string function as account numbers are stored as strings
# Use negative indexes to start the slice from the end of the string (as we want to display last 4 digits of acc number)
# Display first 6 digits as 'X', I simply created another variable masked_account number = letter X multiplied by 6 since we are maskind the first 6 digits
# Added \t for good measure

accountnumber = str(input("\tPlease enter 10 digit account number: "))
masked_accountnumber = 'X' * 6 + accountnumber[-4:]
print(f"\tAccount number is {masked_accountnumber}")

# Extra: I asked ChatGPT how to do that and it suggested what I wrote in line 16. This solution will always add the total digits of the number in Xs plus
# the last 4 visible digits. I couldn't figure out how to make Xs represent the masked numbers minus the visible digits

accountnumber = str(input("Please enter account number: "))
list_size = len(accountnumber)
masked_accountnumber = 'X' * list_size + accountnumber[-4:]
print(f"Account number is {masked_accountnumber}")
