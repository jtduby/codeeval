#!/usr/bin/env python

"""
    Discount Offers Solution: v0.1

    Brute force, could use some memoization and short-circuiting. But, to
    paraphrase a wise professor "First things first. Get the damn thing
    working before worrying about how to make it work better".

    Assumptions:

    Version History:
        0.1:    Brute-force

    =================================
    Copyright 2012, Jamie Thomas Duby
    =================================

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
  
    http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import sys
import re
import itertools

def consonants(s):
    """Takes a string s, returns the integer count of consonants in the
    string. Compiling the pattern so I can use a flag.
    """
    r = re.compile('[^BCDFGHJKLMNPQRSTVWXZ]', re.IGNORECASE)
    count = len(re.sub(r, '', s))
    return count

def common_factor_score(name, item, ss):
    """Takes the strings name, item, and the int ss. If the number of letters
    in name and item have a common factor, ss is multiplied by 1.5. Int ss is
    returned to caller.
    """
    n = letters(name)
    i = letters(item)
    if (has_common_factors(n, i)):
        return (ss * 1.5)
    return ss
 
def even_score(name, item):
    """Takes strings name, item. If the number of letters in item is even,
    the number of vowels * 1.5 is returned to the caller.
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

def find_max_scores(names, item_perm, ss_dict):
    """Please, please don't give me too many inputs. Have mercy. I'm just a 
    lowly brute-firce solution.
    """
    max_ss = 0.0
    for p in item_perm:
        temp_ss = 0.0
        for i in range(0, len(names)):
            name = names[i]
            item = p[i]
            temp_ss += ss_dict[name][item]
        if temp_ss > max_ss:
            max_ss = temp_ss
    return max_ss

def find_max_scores2(items, name_perm, ss_dict):
    """This is a bad solution to my oversight, and I feel bad for doing it.
    """
    max_ss = 0.0
    for p in name_perm:
        temp_ss = 0.0
        for i in range(0, len(items)):
            name = p[i]
            item = items[i]
            temp_ss += ss_dict[name][item]
        if temp_ss > max_ss:
            max_ss = temp_ss
    return max_ss

def find_scores(name, items):
    """Takes a string name, and a list of strings items. Returns a dict
    containing S scores that are indexed by the items where 
    SS = ss(name, item) 
    """
    s = {}
    for i in items:
        s[i] = gen_ss(name, i)
    return s 
    
def gen_permutations(names, items, hack=False):
    """Takes a list of string names and a list of string items. Returns
    len(name) sized permutations of items.
    """
    if (not hack):
        p = itertools.permutations(items, len(names))
    else:
        p = itertools.permutations(names, len(items))
    return p        

def gen_ss_dict(names, items):
    """Takes a list of string names and a list of strings items. Returns a
    dict that is indexed by name, and contains dicts of items as returned
    from find_scores().
    """
    s = {}
    for n in names:
        s[n] = find_scores(n, items)
    return s

def gen_ss(name, item):
    """Takes the name and item as strings. Returns the maximum SS."""
    e_score = even_score(name, item)
    o_score = odd_score(name, item)
    eo_score = max(e_score, o_score)
    ss = common_factor_score(name, item, eo_score)
    return ss

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
    """Takes a string s. If the count of letters in s is even, True is
    returned to the caller. Otherwise, False is returned.
    """
    let_count = letters(s)
    if (let_count%2 == 0):
        return True
    return False

def letters(s):
    """Takes a string s, returns the integer count of letters in the string.
    """
    # count = len(re.sub('[^A-Za-z]', '', s))
    count = len(re.sub('[^A-Za-z]', '', s))
    return count

def odd_score(name, item):
    """
    """
    if (not is_even(item)):
        c = consonants(name)
        return c
    return 0.0

def parse_test_line(s):
    """Takes the string line from the test file. Returns a list of names and a
    a list of items. Test string is assumed to be formatted correctly.
    """
    names, items = s.strip().split(";")
    name_list = names.split(",")
    item_list = items.split(",")
    return name_list, item_list

def pretty_print(scores):
    """Prints scores as floats with 2 places after the decimal.
    """
    for s in scores:
        print("%0.2f" % s)

def run_test(infile):
    """I failed to take into account that len(items) may be less than 
    len(names). Got a little hacktastic to fix this. Code will need to be
    refactored before I optimize.
    """
    scores = []
    for line in infile:
        names, items = parse_test_line(line)
        ss_dict = gen_ss_dict(names, items)
        if (len(items) >= len(names)):
            item_perms = gen_permutations(names, items)
            scores.append(find_max_scores(names, item_perms, ss_dict))
        else:
            name_perms = gen_permutations(names, items, True)
            scores.append(find_max_scores2(items, name_perms, ss_dict))
    return scores

def vowels(s):
    """Takes the string s. Return the integer count of vowels in the string.
    """
    count = len(re.sub('[^AEIOUYaeiouy]', '', s))
    return count

if  __name__ == '__main__': 
    infile = open(sys.argv[1], 'r')
    scores = run_test(infile)
    infile.close()
    pretty_print(scores)
    sys.exit(0)

sys.exit(1)
