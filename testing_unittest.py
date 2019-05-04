#!/usr/bin/env python3

import unittest

def foo(arg: int) -> int:
    return arg*arg

class MyTestClass(unittest.TestCase):
    def setUp(self):
        # this is run before every test
        self.bar = 0

    def test_sample(self):
        self.assertEqual(foo(3), 9)

    def test_sample_should_fail(self):
        self.assertEqual(foo(3), 8)

    def this_wont_be_tested_because_it_doesnt_start_with_test(self):
        self.assertEqual(foo(3), 999)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
