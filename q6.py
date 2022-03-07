import math

def sieve(n):
    prime_list = [2]

    if n <= 1:
        return []

    if n == 2:
        return prime_list

    x = 3

    while x <= math.sqrt(n):
        is_prime = True
        for prime in prime_list:
            if x % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_list.append(x)

        x += 2

    count = len(prime_list)

    for i in range(prime_list[0] + 1, n + 1):
        is_prime = True
        for j in range(count):
            if i % prime_list[j] == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(i)

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

    i = 2
    
    # All prime factors of n are smaller than sqrt(n). Therefore if i is a
    # prime factor of n then i <= sqrt(n) -> i^2 <= n.
    while i <= math.sqrt(n):
        if n % i == 0:
            return False

        i += 1


    return True


for i in range(1, 100):
    if is_prime(i):
        print(str(i))


sieve(3)
sieve(10)
sieve(11)
sieve(100)
