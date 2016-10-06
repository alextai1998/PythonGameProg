import numpy as np


def square(a):
    return a**2

inputs = list(np.random.rand(10))
print(inputs)
squares = list(map(square, inputs))  # grow the list one element at a time

print(squares)
