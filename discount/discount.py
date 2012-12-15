#!/usr/bin/env python

"""
    Discount Offers Solution: v0.1

    Brute force, could use some memoization and short-circuiting. But, to
    paraphrase a wise professor "First things first. Get the damn thing
    working before worrying about how to make it work better".

    Assumptions:
        --> Number of items >= number of customers as a given product may only
            be offered to one customer.
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

def common_factor_score(name, item):
    """
    """
    n = letters(name)
    i = letters(i)
    if (has_common_factors(n, i)):
        return (n * 1.5)
    return 0.0
 

def even_score(name, item):
    """
    """
    if (is_even(item)):
        v = vowels(name)
        return (v * 1.5)
    return 0.0

def find_factors(n):
    """Takes and integer n, returns the set of all factors of n, except 1."""
    f = set([n])
    for i in range(2, n):
        if (n%i == 0):
            f.add(i)
    return f

def gen_ss(name, item):
    """Takes the name and item as strings. Returns the maximum SS."""
    cf_score = common_factor_score(name, item)
    e_score = even_score(name, item)
    o_score = odd_score(name, item)
    return max(cf_score, e_score, o_score)

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

def is_even(s):
    """
    """
    let_count = letter(s)
    if (let_count%2 == 0):
        return True
    return False

def letters(s):
    """Takes a string s, returns the integer count of letters in the string.
    """
    count = len(re.sub('[^A-Za-z]', '', s))
    return count

def odd_score(name, item):
    """
    """
    if (not is_even(item)):
        c = consonants(name)
        return (c * 1.5)
    return 0.0

def parse_test_line(s):
    """Takes the string line from the test file. Returns a list of names and a
    a list of items. Test string is assumed to be formatted correctly.
    """
    names, items = s.split(";")
    name_list = names.split(",")
    items_list = items.split(",")
    return names_list, items_list

def vowels(s):
    """Takes the string s. Return the integer count of vowels in the string.
    """
    count = len(re.sub('[^AEIOUaeiou]', '', s))
    return count

 __name__ == '__main__': 
    test_cases = open(sys.argv[1], 'r')

    for line in test_cases:
    test_cases.close()
    f = Factors()
    sys.exit(0)

sys.exit(1)
