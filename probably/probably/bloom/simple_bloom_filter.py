# -*- coding: utf-8 -*-

import mmh3 as murmur
import math
from ..core import BitVector
import itertools

class SimpleBloomFilter(object):
    def __init__(self, expected_capacity, false_positive_probability):

        num_bits = long(math.ceil(-expected_capacity* math.log(p) / (math.log(2) ** 2)))
        num_hash_funcs = num_bits/expected_capacity * math.log(2)

    	self.capacity = (num_bits / 8 ) * 8 # Round to nearest multiple of 8
        self.bit_set = bytearray(self.capacity / 8)
        self.hash_funcs = [make_hash_function(i) for i in range(num_hash_funcs)]

    def add(self, value):
    	for i in self._get_indices(value):
    		self.bit_set[i] = 1

    def contains(self, value):
    	return all([self.bit_set[index] for index in self._get_indices(value)])

    # Returns the indices in the bitset associated with a particular value
    def _get_indices(self, value):
    	return [f(value) % self.capacity for f in self.hash_funcs]


# Creates a hash function for a given hash_func_number.
def make_hash_function(hash_func_number):
	def salted_hash_func(value):
		return murmur.hash('%s' % (value), hash_func_number)
	return salted_hash_func