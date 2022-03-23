# For this solution I am using a well-known method developed by
# Netwon to find approximate solutions for the roots of
# eqations. Specifically, I am finding an approximation for the
# root of y = x^2 - c. That means that I am solving for when y =
# 0 i.e. 0 = x^2 - c => sqrt(c) = x. Hence, by solving the
# following equation you are finding an approximation for the
# sqrt(c).

# In this case the algorithm has a time-complexity of O(n) where
# n depends on the input.
#
# We need iteration to ensure that the approximation is
# reasonably accurate.
#
# If the domain of the function was bounded, we could make the
# algorithm O(1) by alwalys making the function iterate a
# sufficient number of times for all the values in the given
# domain.


import math


# This function is the acutal answer.
def newton_sqrt(n):
    if n < 0:
        return -1

    x = n

    for i in range(max(math.floor(n), 5)):
        x = x - (x**2 - n) / (2 * x)

    return x


# https://en.wikipedia.org/wiki/Halley's_method

# This is an interesting optimisation (increaseing the rate at
# which the function converges).
def halley_sqrt(n):
    if n < 0:
        return -1

    x = n

    for i in range(math.floor(n)):
        x = x - (2 * (x**2 - n) * (2 * x)) / (8 * (x**2) - 2 * (x**2 - n))

    return x
