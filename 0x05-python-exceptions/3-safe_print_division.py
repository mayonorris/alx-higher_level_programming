#!/usr/bin/python3

def safe_print_division(a, b):
 """Divides two integers and prints the result within a finally block."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return (None)
    except Exception:
        print("Inside result: {}".format(None))
        return (None)
    else:
        print("Inside result: {}".format(result))
        return (result)
    finally:
        print("Inside result: {}".format(result))

