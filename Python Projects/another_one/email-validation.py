import re

email_conditions = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input("Enter your email address: ")

if re.search(email_conditions, user_email):
    print("Email is perfect")
else:
    print("Email is in wrong format")