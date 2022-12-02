#!/usr/bin/python3

def element_at(my_list, idx):
    """Access element at a given index"""
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return(my_list[idx])
