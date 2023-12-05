#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    my_list_copy = my_list.copy()

    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list_copy)

    del(my_list_copy[idx])
    return (my_list_copy)
