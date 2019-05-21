#!/usr/bin/env python3

def try_assert(evalstr):
    try:
        print(f'Evaluating: {evalstr}')
        assert(eval(evalstr))
        print(f'SUCCESS')
    except AssertionError:
        print(f'FAILURE')

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

