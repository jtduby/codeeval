#!/usr/bin/env python

"""
    Prefix Expressions Solution: v0.1
"""
import sys

class Stack(object):
    def __init__(self):
        self.s = []
    def push(self, obj):
        self.s.append(obj)
    def pop(self):
        if self.size() > 0:
            return self.s.pop() 
        else:
            return None
    def size(self):
        return len(self.s)

class Operations(object):
    def __init__(self):
        self.ops = {"+": (lambda x,y: x + y),
                    "*": (lambda x,y: x * y),
                    "/": (lambda x,y: x / y)}
    def perform(self, expr):
        op, x, y = expr
        result = self.ops[op](x, y)
        return result
 
class Calculator(object):
    def __init__(self):
        self.s = Stack()
        self.o = Operations()
    def calculate(self, op):
        y = self.s.pop()
        x = self.s.pop()
        result = self.o.perform((op, x, y))
        self.s.push(result)
    def evaluate(self, eq_str):
        eq_list = self.make_eq_list(eq_str)
        for item in eq_list:
            if item.isdigit():
                self.s.push(int(item))
            else:
                self.calculate(item)
        return self.s.pop()
    def make_eq_list(self, eq_str):
        tmp_str = eq_str.strip()
        # print tmp_str
        eq_list = tmp_str.split()
        eq_list.reverse()
        return eq_list

if __name__ == '__main__': 
    test_cases = open(sys.argv[1], 'r')
    c = Calculator()

    for line in test_cases:
        r = c.evaluate(line)
        print r        
    test_cases.close()

    sys.exit(0)

sys.exit(1)
