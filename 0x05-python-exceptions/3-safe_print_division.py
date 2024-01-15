#!/usr/bin/python3

def safe_print_division(a, b):
 """Divides two integers and prints the result within a finally block."""

 result = None

 try:
   result = a / b
 except (TypeError, ZeroDivisionError):
   print("Error: Cannot divide by zero!")
 finally:
   print("Inside result: {}".format(result))

 return (result)

