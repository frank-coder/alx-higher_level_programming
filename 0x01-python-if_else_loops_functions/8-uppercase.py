#!/usr/bin/python3

def uppercase(str):
    """uppercase converts string to uppercase."""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
            print(f"{i}", end="")
    print()
