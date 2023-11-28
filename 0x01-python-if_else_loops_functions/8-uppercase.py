#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
        # Convert the lowercase letter to uppercase using ASCII manipulation
        uppercase_char = chr(ord(char) - 32)
        print(uppercase_char, end="")
        else:
            print(char, end="")
    print()  # Print a newline at the end
