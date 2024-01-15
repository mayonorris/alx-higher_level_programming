#!/usr/bin/python3

def safe_print_division(a, b):
 """Divides two integers and prints the result within a finally block."""

    try:
        res = a / b
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return (res)
