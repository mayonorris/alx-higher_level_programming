#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key  in list(a_dictionary):
        a_dictionary[key] = 2*a_dictionary[key]
    return (a_dictionary)
