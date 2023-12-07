#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary = a_dictionary.copy()
    keys =  list(a_dictionary)

    for key  in keys:
        a_dictionary[key] *= 2

    return (a_dictionary)
