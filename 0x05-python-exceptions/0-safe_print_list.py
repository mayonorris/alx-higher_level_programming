#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    # Use a try-except block to handle exceptions
    try:
        # Iterate through the list and print elements up to x
        for i in range(x):
            print(my_list[i], end=" ")
            elements_printed += 1

    except IndexError:
        # Handle the case where the index is out of range
        pass

    finally:
        # Print a new line after the elements
        print()

    # Return the real number of elements printed
    return (elements_printed)

