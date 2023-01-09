#!/usr/bin/python3
"""inherits_from
"""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified
    class ; otherwise False.
    """

    if issubclass(obj, a_class):
        return True
    return False
