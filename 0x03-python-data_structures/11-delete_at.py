#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete an element at a given index of a list"""
    if idx < 0 or idx > len(my_list):
        return(my_list)
    else:
        del(my_list[idx])
        return(my_list)
