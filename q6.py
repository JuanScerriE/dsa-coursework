from math import sqrt
from math import ceil

# The idea: Basically, we are going to create an array whose size is given by
# our input. in this case `limit`. The array will be filled with `True` or
# `False`. `True` denotes that the index used to access that location in the
# array is a prime. `False` denotes that the index used to access that location
# in the array is not prime. The first two indicies 0 and 1 are not prime and
# they are set to `False`.

# Starting from index 2. If the value at index n is `True` then mark every
# multiple of n (2n, 3n, 4n, etc.) until the limit as `False`. Essentially,
# striking them out. Repeat the process for all indicies.

# At the end you will have effectively struck out all the indicies which are
# not prime.

# Optimisation 1: The initialisation pattern is usually all [False, False,
# True, True, True, ...]. Instead we can start with [False, False, True, False,
# True, False, True, False, ...]. This means that we are already discounting
# half of the array. This is true because this pattern concides with the the
# pattern of even and odd numbers. And as we know every even number which is
# not 2 is not prime.

# Optimisation 2: We do not need to check every element until we reach the
# limit. We can check uptill the square root of the limit to find all prime
# numbers uptill the limit. This is possible because no the compositie numbers
# smaller than our limit can have prime factors which are larger than their own
# square root and since they are smaller than our limit then their square root
# of is also smaller than the square root of the limit. Therefore all composite
# numbers uptill the limit must have factors which are samller than the square
# root of the limit.

# Optimisation 3: We can start crossing out from the square of the index. This
# is because anything smaller than the square of our index is either prime or
# has a prime factor which is smaller than our index therefore it would have
# already been dealt with. This again uses the same property that any integer
# which is not prime has a prime factor which is samller than or equal to its
# square root. And any element smaller than the square of our index
# automatically implies that it is either prime or has a factor which is
# smaller than our index.

def f_sieve(limit):
    # Optimistaion 1
    N = [False, True] * ((limit + 1) // 2)

    N[1] = False; N[2] = True

    # Optimisation 2
    for n in range(3, ceil(sqrt(limit)), 2):
        if N[n]:
            # Optimistaion 3
            for m in range(n*n, limit, n):
                N[m] = False

    P = []

    for n in range(limit):
        if N[n]:
            P.append(n)

    return P



def sieve(n):
    prime_list = [2]

    if n <= 1:
        return []

    if n == 2:
        return prime_list


    # Finding all primes smaller than sqrt(n).

    # Note: the upperbound will be ceil(sqrt(n)) since e.g. sqrt(24) ~ 4.89
    # which means that we check 3 and 4 but the range function those not
    # include the upperbound so we have to compensate by incrementing by one.
    # Hence why ceil() is used.

    for x in range(3, ceil(sqrt(n)), 2):
        is_prime = True
        # Checking if x is prime by checking against previous primes. If no
        # previous prime divides x then x is prime.
        for prime in prime_list:
            if x % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_list.append(x)


    count = len(prime_list)

    # Finding the rest of the primes by sieving the integers which are
    # divisible by the initial collection of primes.
    for x in range(prime_list[0] + 1, n + 1):
        is_prime = True
        for i in range(count):
            if x % prime_list[i] == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(x)

    return prime_list

def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True
    
    # We check if it is even and not 2. If so then is it is definitely not
    # prime.
    if n % 2 == 0:
        return False
    
    # All prime factors of n are smaller than sqrt(n). Therefore if i is a
    # prime factor of n then i <= sqrt(n).
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            return False

    return True


for i in range(1, 100):
    if is_prime(i):
        print(str(i))

print(sieve(3))
print(sieve(7))
print(sieve(24))
print(sieve(97))
print(f_sieve(98))
