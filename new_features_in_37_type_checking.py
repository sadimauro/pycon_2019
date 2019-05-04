# 
# Dynamic typing
#
def foo(arg1, arg2):
    return "foo"*arg1 + " " + arg2

print(foo(3, "FOO"))

# The first argument is intended to be an int but is a string below
try:
    foo("oops", "FOO")
except TypeError as e:
    print(f"using 'oops' as first arg: {e}")

# The return is intended to be a string but is assumed to be an int below
try:
    ret = foo(3, "FOO")
    print(ret + 99)
except TypeError as e:
    print(f"assuming return of foo() is an int: {e}")


#
# Static typing
#
def foo(arg1: int, arg2: str) -> str:
    return "foo"*arg1 + " " + arg2

print(foo(3, "FOO"))

# This should be caught by mypy?
foo("oops", "FOO")

# This should be caught by mypy?
ret = foo(3, "FOO")
some_sum = ret + 99
