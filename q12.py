# 12. Write a function that returns the sum of the first n numbers of the
# Fibonacci Sequence. The first 2 numbers in the sequence are 1, 1.

# I am using the closed-form expression for the Fibonacci Sequence to get the
# exact value at index n without having to compute all the previous elements of
# the sequence.

# Moreover, I am using the close-form expression for the sum of the elements in
# the sequence to get the exact sum at index n without having to add all
# previous elements. This makes the algorithm O(1).

import math

def fib(n):
    return math.floor((((1 + math.sqrt(5)) / 2) ** n) / math.sqrt(5) + 0.5)

def sum_fib(n):
    return fib(n + 2) - 1

def sum_fib_iter(n):
    sum = 0

    for i in range(1, n + 1):
        sum += fib(i)


    return sum

print("Fibonacci Sequence\n")

# Fibonacci Sequence
for i in range(1, 10):
    print("n = " + str(i) + ": " + str(fib(i)))

print("\nFibonacci Sum Iterative\n")

# Fibonacci Sum Iterative O(n)
for i in range(1, 10):
    print("n = " + str(i) + ": " + str(sum_fib_iter(i)))


print("\nFibonacci Sum O(1)\n")

# Fibonacci Sum O(1)
for i in range(1, 10):
    print("n = " + str(i) + ": " + str(sum_fib(i)))
