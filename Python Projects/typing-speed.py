from time import time
import random as r

def mistake_finder(para_test, user_test):
    error = 0
    for i in range(min(len(para_test), len(user_test))):
        if para_test[i] != user_test[i]:
            error += 1
    return error

def speed_time_fnc(time_s, time_e, user_input):
    time_delay = (time_e - time_s)
    time_round = round(time_delay, 2)
    speed = len(user_input) / time_round
    return round(speed)

test = ["Ore o sonta putu dekha tor kaila pasuu", "My name is foty"]

test_1 = r.choice(test)

print("***** Typing Speed *****")
print(test_1)
print()

time_1 = time()
test_input = input("Enter your sentences: ")
time_2 = time()

print("Your Speed was:", speed_time_fnc(time_1, time_2, test_input), "WPS")

print("Errors were:", mistake_finder(test_1, test_input))
