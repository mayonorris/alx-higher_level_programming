#!/usr/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary = a_dictionary.copy()
    if key not in list(a_dictionary):
        return (a_dictionary)
    del(a_dictionary)[key]
    return (a_dictionary)
