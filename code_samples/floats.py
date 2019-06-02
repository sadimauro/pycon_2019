#!/usr/bin/env python3

def try_assert(evalstr):
    try:
        print(f'Evaluating: {evalstr}')
        assert(eval(evalstr))
        print(f'SUCCESS')
    except AssertionError:
        print(f'FAILURE')

def print_and_eval(evalstr):
    print(f'Evaluating: {evalstr}')
    print(eval(evalstr))

# Floats are stored as a sign bit, exponent bits ('scaling factor' = the point 'floats'),
# and the fractional part ('mantissa').
#
# The mantissa is stored as base-2, so numbers that can be represented as a 
# (reasonably-)finite sequence of base-2 integers can be represented exactly.

a = 0.5
b = 0.25
c = 0.75

try_assert('a + b == c')

x = 0.1
y = 0.2
z = 0.3

try_assert('x + y == z')

# math.fsum() 'tracks multiple intermediate partial sums'.
import math
try_assert('math.fsum((x, y)) == z')

# numpy.sum is another floating point summer
import numpy
try_assert('numpy.sum((x, y)) == z')

# numpy.isclose() calculates whether or not floating point numbers are equal within
# a given tolerance.
try_assert('numpy.isclose(numpy.sum((x, y)), z)')

# The decimal module provides good default precision and sensible rounding
from decimal import Decimal
xd = Decimal(str(x))
yd = Decimal(str(y))
zd = Decimal(str(z))
try_assert('xd + yd == zd')

# Other funny things happen

# Precision vs. magnitude tradeoff
try_assert('1e20 + 1 == 1e20')

print_and_eval('12345 + 1e15')
print_and_eval('12345 + 1e16')
print_and_eval('12345 + 1e17')

i = float("inf")
print_and_eval('i')
print_and_eval('i + i')
print_and_eval('i > 10e10')
print_and_eval('i > 10e307')
print_and_eval('i > 10e308')
print_and_eval('i / i')

n = float('nan')
print_and_eval('n')
print_and_eval('n == n')
print_and_eval('1 > n')
print_and_eval('1 < n')
print_and_eval('1 == n')
print_and_eval('1 + n')
print_and_eval('n in [n]')

