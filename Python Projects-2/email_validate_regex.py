import re

email_cond = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_input = input("Enter your email: ")

if re.search(email_cond, user_input):
    print("Right email")
else:
    print("Wrong emails")