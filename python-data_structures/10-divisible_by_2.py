#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list, returning a list of booleans."""
    result = []
    for n in my_list:
        result.append(n % 2 == 0)
    return result
