#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = my_list.copy()
    for idx, val in enumerate(my_list):
        if val == search:
            my_list[idx] = replace
    return (my_list)
