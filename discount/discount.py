#!/usr/bin/env python

"""
    Discount Offers Solution: v0.1

    Brute force, could use some memoization and short-circuiting. But, to
    paraphrase a wise professor "First things first. Get the damn thing
    working before worrying about how to make it work better".
"""
import sys
import re

def consonants(s):
    """Takes a string s, returns the integer count of consonants in the
    string. Compiling the pattern so I can use a flag.
    """
    r = re.compile('[^BCDFGHJKLMNPQRSTVWXYZ]', re.IGNORECASE)
    count = len(re.sub(r, '', s))
    return count

def find_factors(n):
    """Takes and integer n, returns the set of all factors of n, except 1."""
    f = set([n])
    for i in range(2, n):
        if (n%i == 0):
            f.add(i)
    return f

def has_common_factors(x, y):
    """Takes two integers, x and y. Returns True if they have common factors,
    False if they do not.
    """
    fact_x = find_factors(x)
    fact_y = find_factors(y)
    cf = fact_x & fact_y
    if (len(cf) > 0):
        return True
    return False

def letters(s):
    """Takes a string s, returns the integer count of letters in the string.
    """
    count = len(re.sub('[^A-Za-z]', '', s))
    return count

def parse_test_line(s):
    """Takes the string line from the test file. Returns a list of names and a
    a list of items. Test string is assumed to be formatted correctly.
    """
    names, items = s.split(";")
    name_list = names.split(",")
    items_list = items.split(",")
    return names_list, items_list

 __name__ == '__main__': 
    test_cases = open(sys.argv[1], 'r')

    for line in test_cases:
    test_cases.close()
    f = Factors()
    sys.exit(0)

sys.exit(1)
