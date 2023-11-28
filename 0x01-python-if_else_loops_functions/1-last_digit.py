#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = -1 * (abs(number) % 10)
else:
    last_digit = number % 10
output_start = "Last digit of {} is".format(number)
if last_digit > 5:
    print(output_start + " {} and is greater than 5".format(last_digit))
elif last_digit == 0:
    print(output_start + " {} and is 0".format(last_digit))
elif last_digit < 6 and not 0:
    print(output_start + " {} and is less than 6 and not 0".format(last_digit))
