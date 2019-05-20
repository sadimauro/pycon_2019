#!/usr/bin/env python3

import time

def timer(fun):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = fun(*args, **kwargs)
        
        total_time = time.time() - start_time
        print(f'[{fun.__name__} took {total_time} sec to run]')
        
        return result
    return wrapper

@timer
def fast_int_add(x, y):
    return x + y

@timer
def slow_int_add(x, y):
    result = x
    for i in range(y):
        result += 1
    return result

if __name__ == '__main__':
    x = 100000
    y = 100000
    print(slow_int_add(x, y))
    print(fast_int_add(x, y))
