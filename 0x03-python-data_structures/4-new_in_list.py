#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element of a list at a given index without
    modifying the original list"""
    new_list = my_list[:]
    if idx < 0 or idx > len(new_list) - 1:
        return new_list
    else:
        new_list[idx] = element
        return new_list
