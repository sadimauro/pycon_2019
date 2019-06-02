#!/usr/bin/env python3

import time

# Instead of using '=' which just assigns, ':=' assigns and returns
# a value, enabling the user to use it with if/while statements and 
# in other places.

def timer(fun):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = fun(*args, **kwargs)
        
        total_time = time.time() - start_time
        print(f'[{fun.__name__} took {total_time} sec to run]')
        
        return result
    return wrapper

# Each of the three 'options' returns a three-long list of
# results from calling fun with arg x.  The third option, using
# the assignment operator, should be the fastest.

@timer
def option_1(fun, x):
    return [fun(x), fun(x)**2, fun(x)**3]

@timer
def option_2(fun, x):
    y = fun(x)
    return [y, y**2, y**3]

@timer
def option_3(fun, x):
    return [y := fun(x), y**2, y**3]

def some_fun(x):
    g = 2
    mod = 104729
    ival = 1
    for i in range(x):
        ival = (ival*g) % mod
    return ival

# The assignment operator simplifies file reading, and should make
# it faster, too.
@timer
def process_file_option_1(fp, process):
    chunk = fp.read(8192)
    while chunk:
        process(chunk)
        chunk = fp.read(8192)

@timer
def process_file_option_2(fp, process):
    while chunk := fp.read(8192):
        process(chunk)

if __name__ == '__main__':
    x = 100000
    print(option_1(some_fun, x))
    print(option_2(some_fun, x))
    print(option_3(some_fun, x))

