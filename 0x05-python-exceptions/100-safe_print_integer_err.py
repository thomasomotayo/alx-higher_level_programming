#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    '''Prints on integer with "{:d}".format().
    if a ValueError message is caught, a correspoding 
    message is printed to standard error.
    Args:
        valuee (int(: The integer to print.
    Returns
        if a TypeError or valueError occurs - False
        Otherwise - True.'''
    try:
        print("{:d}".format(value))
        return(True)
    except (TypeError, ValueError(:
        print("Exception: {}".format(sys.exc_info()[1]), file = sys.stderr)
        return(False)
