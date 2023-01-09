#!/usr/bin/python3
"""MyList
"""


class MyList(list):
    """ MyList class
    """

    def print_sorted(self):
        """ print_sorted prints the list, but sorted
        (ascending sort)
        """

        print(sorted(self))
