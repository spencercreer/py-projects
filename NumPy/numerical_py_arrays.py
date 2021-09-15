"""
Advantages: NumPy Array over List
1) No for loops to iterate through entire array
2) Faster execution
    a) Single type for each field to avoid type checking
    b) Uses contiguous blocks of memory
3) Uses less memory
"""

import numpy as np
from numpy.core.numeric import ones

# ways to create a numpy array
# pass a list
a = np.array([(2,3,4), (5,6,7)], dtype=np.int16)
print('a: \n', a)
# arange function (from, to, step)
b = np.arange(1, 12, 2)
print('\nb: \n', b)
# linear spacing: creates a floating point array
# linspace(from, to, number of equally spaced elements) 
c = np.linspace(1, 12, 6)
print('\nc: \n', c)

# reshape function returns a matrix reshape(rows, columns)
c = c.reshape(3,2)
print('\nc reshaped: \n', c)

# return size
print('\nsize of a: ', a.size)
# return shape e.g. (rows, columns)
print('\nc (rows, columns): ', c.shape)
# return datatype and itemsize
print('\ndatatype of a: ', a.dtype)
print('itemsize of a: ', a.itemsize, ' bytes')
print('datatype of b: ', b.dtype)
print('itemsize of b: ', b.itemsize, ' bytes')
print('datatype of c: ', c.dtype)
print('itemsize of c: ', c.itemsize, ' bytes')
# quickly iterate through an array
print('\na<4: \n', a<4)
print('\na x 3 = \n', a*3)
# methods to generate arrays
zeros_array = np.zeros((3,3))
print('\narray of zeros: \n', zeros_array)
ones_array = np.ones((3,2))
print('\narray of ones: \n', ones_array)
# random arrays
random_array = np.random.random((2,3))
print('\nrandom array: \n', random_array)
np.set_printoptions(precision=2, suppress=True)
print('\nrandom array rounded two decimals: \n', random_array)
rand_int_array = np.random.randint(0,10,5)
print('\nrandom integer array: \n', rand_int_array)
# statistics methods
print('random integer array sum: ', rand_int_array.sum())
print('random integer array min: ', rand_int_array.min())
print('random integer array max: ', rand_int_array.max())
print('random integer array mean: ', rand_int_array.mean())
print('random integer array varience: ', rand_int_array.var())
print('random integer array standard deviation: ', rand_int_array.std())
# load in file
data = np.loadtxt('data.txt', dtype=np.uint8, delimiter=',', skiprows=1)
print('\nloaded txt file array: \n', data)
