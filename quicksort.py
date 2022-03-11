import math
import random
import sys

sys.setrecursionlimit(5000)

def swap(a, x, y):
    t = a[x]
    a[x] = a[y]
    a[y] = t
 

def nexth(n, m):
    return 2 * int(math.floor(n / 2 ** (m + 1))) + 1


def shellsort(a):
    n = len(a)
    m = 1
    h = nexth(n, m)

    while h >= 1:
        for i in range(h):
            for j in range(i + h, n, h):
                for k in range(j, i, -h):
                    if a[k] < a[k - h]:
                        swap(a, k, k - h)
                    else:
                        break

        m += 1

        if h == 1:
            break

        h = nexth(n, m) 
   
    return a

def pivot(a, i, j):
    n = []

    for k in [random.randint(i, j) for k in range(7)]:
        n.append(a[k])

    shellsort(n)
    
    return n[3]


def partition(a, i, j):
    p = pivot(a, i, j)
    i -= 1
    j += 1

    while True:
        while True:
            i += 1
            if a[i] >= p:
                break

        while True:
            j -= 1
            if a[j] <= p:
                break

        if i >= j:
            return j

        swap(a, i, j)

def quicksort(a, i, j):
    if 0 <= i < j:
        p = partition(a, i, j)
        quicksort(a, i, p)
        quicksort(a, p + i, j)


a = [23,3,5,4,656,3,5,56,53,4,5,656,75,334,23]

quicksort(a, 0, len(a) - 1)

print(a)
