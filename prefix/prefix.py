#!/usr/bin/env python

"""
    Prefix Expressions Solution: v0.2

    Evaluates prefix expressions.

    Taken from: http://www.codeeval.com/open_challenges/7/

    Description:

        You are given a prefix expression. Write a program to evaluate it.

    Input sample:

        The first argument will be an input file with one prefix expression 
        per line. e.g.

            * + 2 3 4

        Your program has to read this and insert it into any data structure 
        you like. Traverse that data structure and evaluate the prefix 
        expression. Each token is delimited by a whitespace. You may assume 
        that the only valid operators appearing in test data are '+','*' 
        and '/'

    Output sample:

        Print to stdout, the output of the prefix expression, one per line. e.g.

            20


    Version History:
        0.2: Cleaned code, fixed dcoumentation.

    ======================================
    Copyright 2012,2013  Jamie Thomas Duby
    ======================================

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

class Stack(object):
    """Simple stack implementation. 

        *Note* This challenge was completed before the stack implementation
               challenge. That stack was modified from this one, and not 
               vice-versa. This one isn't as robust, but it doesn't need to
               be, so I'm leaving it alone.
    """
    def __init__(self):
        """Initializes an empty stack."""
        self._s = []
    def push(self, obj):
        """Pushes an object onto the stack.
        """
        self._s.append(obj)
    def pop(self):
        """Pops an item from the stack.

        Didn't bother to make this safe. Technically, I could have checked
        an empty stack and returned Null, or raised an exception. But, if we
        are popping from an empty stack here, the infile is malformed, so
        failing loudly is in order.
        """
        return self._s.pop() 
    def empty(self):
        """If the stack is empty, returns True. Otherwise, False."""
        if len(self._s) > 0:
            return False
        else:
            return True

class Operations(object):
    """Evaluates a tuple containing a single, i.e. two operands and an 
    operation, arithmetic expression.

    Implemented are addition, multiplication, and division. CodeEval
    specifications explicitly ommitted subtract, so it is not handled here.
    """
    def __init__(self):
        """This string operation symbol evaluates to it's respective 
        operation.

        While I like lambdas, I realize that they don't usually lead to
        easily readable code. The _ops implementation is one of those 
        exceptions. 
        """
        self._ops = {"+": (lambda x,y: x + y),
                     "*": (lambda x,y: x * y),
                     "/": (lambda x,y: x / y)}
    def perform(self, expr):
        """Takes a tuple in the form of:

        (<str operation>, <int operand>, <int operand>)

        It evaluates the equation and returns the result to the caller. 
        """
        op, x, y = expr
        result = self._ops[op](x, y)
        return result
 
class Calculator(object):
    def __init__(self):
        """Calculator class constructor."""
        self._s = Stack()
        self._o = Operations()
    def _calculate(self, op):
        y = self._s.pop()
        x = self._s.pop()
        result = self._o.perform((op, x, y))
        self._s.push(result)
    def evaluate(self, eq_str):
        """Takes a prefix expression as a string. Evaluates it, and returns
        the result.
        """
        eq_list = self._make_eq_list(eq_str)
        for item in eq_list:
            if item.isdigit():
                self._s.push(int(item))
            else:
                self._calculate(item)
        return self._s.pop()
    def _make_eq_list(self, eq_str):
        tmp_str = eq_str.strip()
        eq_list = tmp_str.split()
        eq_list.reverse()
        return eq_list

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as infile:
        c = Calculator()
        for line in infile:
            r = c.evaluate(line)
            print r        
    sys.exit(0)
