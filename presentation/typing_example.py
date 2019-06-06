# Dynamic typing
def foo_static(arg1, arg2):
    return ("a" * arg1) + " " + arg2

# Static typing
def foo_dynamic(arg1: int, arg2: str) -> str:
    return ("a" * arg1) + " " + arg2

foo_dynamic("oops", "bar")
foo_dynamic(3, "bar") + 99
foo_static("oops", "bar")
foo_static(3, "bar") + 99

x = 1
x = "baz"

import typing
y: typing.List[bool]
y = [True, False, True]
y = [True, "some_string"]
