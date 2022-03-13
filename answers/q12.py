# I am using the closed-form expression for the Fibonacci Sequence to get the
# exact value at index n without having to compute all the previous elements of
# the sequence.

# Moreover, I am using the close-form expression for the sum of the elements in
# the sequence to get the exact sum at index n without having to add all
# previous elements. This makes the algorithm O(1).

from math import floor
from math import sqrt

def fib(n):
    return floor((((1 + sqrt(5)) / 2) ** n) / sqrt(5) + 0.5)

def sum_fib(n):
    return fib(n + 2) - 1
