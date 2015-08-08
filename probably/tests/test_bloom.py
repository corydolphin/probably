#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_probably
----------------------------------

Tests for `probably` module.
"""

import unittest
import sys
import random
import itertools
from probably.bloom import SimpleBloomFilter


def random_gen(low, high):
    while True:
        yield random.randrange(low, high)

gen = random_gen(1, 100)

items = set()

# try to add elem to set until set length is less than 10
for x in itertools.takewhile(lambda x: len(items) < 10, gen): 
    items.add(x)


def generate_unique_random_numbers(minimum=0, maximum=1000, count=10):
    randoms = set()
    while len(randoms) < count:
        randoms.add(random.randint(minimum, maximum))   
    return randoms

class TestProbably(unittest.TestCase):
    def test_accuracy(self):
        bloom = SimpleBloomFilter(100000,10)
        test_integers = generate_unique_random_numbers(0,sys.maxint, 20000)

        errors = 0
        for i, test_integer in enumerate(test_integers):
            errors += bloom.contains(test_integer)
            bloom.add(test_integer)
            if i % 100 == 0:
                print "After %s numbers, a total of %s errors. " % (i, errors)

        # print "Final count: after %s numbers, a total of %s errors. " % (i, errors)


if __name__ == '__main__':
    unittest.main()
