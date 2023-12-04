#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)

    l_max = my_list[0]
    for elt in my_list[1:]:
        if elt > l_max :
            l_max = elt

    return (l_max)
