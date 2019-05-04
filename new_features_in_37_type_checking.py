# Python 3.0 (?) introduced static type checking.
# mypy (Python 3.5+) statically checks type annotations 
# as define din PEP 484.  
#
# More at https://mypy.readthedocs.io

# 
# Dynamic typing
#
def foo(arg1, arg2):
    return "foo"*arg1 + " " + arg2

foo(3, "FOO")

# The first argument is intended to be an int but is a string below
try:
    foo("oops", "FOO")
except TypeError as e:
    print(f"using 'oops' as first arg: {e}")

# The return is intended to be a string but is assumed to be an int below
try:
    ret = foo(3, "FOO")
    some_sum = ret + 99
except TypeError as e:
    print(f"assuming return of foo() is an int: {e}")


#
# Static typing
# Note: the errant calls below should be caught by mypy
#
def foo2(arg1: int, arg2: str = "default value") -> str:
    return "foo"*arg1 + " " + arg2

foo2(4)
foo2(3, "FOO")

cond = "mistakenly calling foo2() with first arg as str instead of int"
try:
    foo2("oops", "FOO")
except TypeError as e:
    print(f"{cond}: {e}")

cond = "mistakenly interpreting return of foo2() as int instead of str"
try:
    ret2 = foo2(3, "FOO")
    some_sum = ret2 + 99
except TypeError as e:
    print(f"{cond}: {e}")

# Annotations include the None type for function returns
def foo3() -> None:
    print('hello world')

cond = "mistakenly storing return of non-returning fn"
try:
    foo3()
except TypeError as e:
    print(f"{cond}: {e}")

# Using the typing module to annotate more complex types
from typing import List
def cat_strs(arg: List[str]) -> str:
    return "".join(arg)

cat_strs(['one', 'two', 'three'])

cond = "mistakenly passing in a tuple instead of a list"
try:
    cat_strs(('one', 'two', 'three'))
except TypeError as e:
    print(f"{cond}: {e}")

