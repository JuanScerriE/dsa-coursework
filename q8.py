# For this solution I am using a well-known method developed by Netwon to find
# approximate solutions for the roots of eqations. Specifically, I am finding
# an approximation for the root of y = x^2 - c. That means that I am solving
# for when y = 0 i.e. 0 = x^2 - c => sqrt(c) = x. Hence, by solving the
# following equation you are finding an approximation for the sqrt(c).

# In this case the algorithm has a time-complexity of O(n) where the n depends
# on the size of the input as naturally as the values become larger you will
# need more iterations to get a good result. If the domain of the function was
# finite, we could make the algorithm O(1) by alwalys making iterate a
# sufficient number of times for all the values in a given domain.

from math import floor

# This function is the acutal answer.
def newton_sqrt(n):
    if n < 0:
        return -1

    x = n

    for i in range(max(floor(n), 5)):
        x = x - (x**2 - n) / (2*x)

    return x

# This is an interesting optimisation (increaseing the rate at which the
# function converges).
def halley_sqrt(n):
    if n < 0:
        return -1

    x = n

    for i in range(floor(n)):
        x = x - (2*(x**2 - n)*(2*x)) / (8*(x**2) - 2*(x**2 - n))

    return x

print("Newton's Method\n")

print("sqrt(2) = " + str(newton_sqrt(2)))
print("sqrt(3) = " + str(newton_sqrt(3)))
print("sqrt(4) = " + str(newton_sqrt(4)))
print("sqrt(5) = " + str(newton_sqrt(5)))
print("sqrt(6) = " + str(newton_sqrt(6)))
print("sqrt(7) = " + str(newton_sqrt(7)))
print("sqrt(8) = " + str(newton_sqrt(8)))
print("sqrt(9) = " + str(newton_sqrt(9)))
print("sqrt(10) = " + str(newton_sqrt(10)))

print("\nHalley's Method\n")

print("sqrt(2) = " + str(halley_sqrt(2)))
print("sqrt(3) = " + str(halley_sqrt(3)))
print("sqrt(4) = " + str(halley_sqrt(4)))
print("sqrt(5) = " + str(halley_sqrt(5)))
print("sqrt(6) = " + str(halley_sqrt(6)))
print("sqrt(7) = " + str(halley_sqrt(7)))
print("sqrt(8) = " + str(halley_sqrt(8)))
print("sqrt(9) = " + str(halley_sqrt(9)))
print("sqrt(10) = " + str(halley_sqrt(10)))
