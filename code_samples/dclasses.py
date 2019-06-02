#!/usr/bin/env python3

import sys
import dataclasses

class MyClass:
    strMember: str
    intMember: int = 99

    def foo(arg: int) -> str:
        return str(arg)

@dataclasses.dataclass
class MyDataclass:
    strMember: str
    intMember: int = 99

    def foo(arg: int) -> str:
        return str(arg)


if __name__ == '__main__':
    x = MyDataclass('X', 1)
    print(x)
    
    # no __init__() created for MyClass
    try:
        y = MyClass('Y', 2)
        print(y)
    except TypeError as e:
        print(e)
        print("Initializing a MyClass object 'manually'")
        y = MyClass()
        y.strMember = 'Y'
        y.intMember = 2


    print(repr(x))
    # no __repr__ defined in MyClass
    print(repr(y))

    import copy
    x_copy = copy.copy(x)
    y_copy = copy.copy(y)

    print(f'x is eq to x_copy: {x == x_copy}')
    print(f'y is eq to y_copy: {y == y_copy}')
