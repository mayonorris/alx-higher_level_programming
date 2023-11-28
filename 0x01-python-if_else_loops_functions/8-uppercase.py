#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 97 <= ord(char) <= 122:
            equival = 32
        else:
            equival = 0
        print("{:c}".format(ord(char)-equival), end="")
    print()
