#!/usr/bin/python3
def fizzbuzz():
    for val in range(1, 101):
        if val % 3 == 0:
            print("Fizz", end = " ")
        elif val % 5 == 0:
            print("Buzz", end =" ")
        elif val % 15 == 0:
            print("FizzBuzz", end = " ")
        else:
            print(val, end = " ")


