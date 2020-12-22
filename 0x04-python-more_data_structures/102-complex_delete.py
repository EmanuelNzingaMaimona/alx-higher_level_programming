#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for x in list(a_dictionary):
        if value == a_dictionary[x]:
            del a_dictionary[x]
    return a_dictionary
