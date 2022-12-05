#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers"""
    if not matrix:
        print()
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j != len(matrix[i]) - 1:
                    end = ' '
                else:
                    end = ''
                print("{:d}".format(matrix[i][j]), end=end)
            print()
