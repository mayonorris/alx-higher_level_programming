#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            equival = 32
        else:
            equival = 0
        print("{:c}".format(ord(char)-equival, end = "")
    print()
