#!/usr/bin/env python3

import sys
import dataclasses

@dataclasses.dataclass
class MyClass:
    strMember: str
    intMember: int = 99

    def foo(arg: int) -> str:
        return str(arg)

def bar(arg: int) -> int:
    return arg*arg

obj = MyClass('object1', 77)

x = bar(10)

print(f'x = {x}')
