#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for val in set(my_list):
        sum += val
    return (sum)
