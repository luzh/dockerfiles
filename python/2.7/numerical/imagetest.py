#!/usr/local/bin/python2.7

from numpy import *

x = array([[1, 2, 3], [4, 5, 6]])
print "Array x has shape",
print x.shape
print x

y = array([[1, 2], [3, 4], [5, 6]])
print "Array y has shape",
print y.shape
print y

dot_product = dot(x, y)
print "Array dot(x, y) has shape",
print dot_product.shape
print dot_product
