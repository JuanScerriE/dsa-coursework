import answers.q1 as q1
import answers.q2 as q2
import random

print("Merge Test")

test1 = [0,1,1,5,3,6,8,7,15,9]
q1.shellsort(test1)

test2 = [0,1,1,5,3,6,8,4,11,9]
q1.quicksort(test2, 0, len(test2) - 1)

test = q2.merge(test1, test2)

if [0,0,1,1,1,1,3,3,4,5,5,6,6,7,8,8,9,9,11,15] == test:
    print("Test Passed\n")
else:
    print("Test Failed\n")

a = []
b = []

len_a = random.randint(256, 300)

len_b = 0

# To make sure they are not of equal length
while True:
    len_b = random.randint(256, 300)

    if len_b != len_a:
        break

# Populate a with random integers
for i in range(len_a):
    a.append(random.randint(0, 1024))

# Populate b with random integers
for i in range(len_b):
    b.append(random.randint(0, 1024))

print("Lenght of a: ", len_a)
print("Lenght of b: ", len_b)

print("\nUnsorted (Shellsort): ", a)
q1.shellsort(a)
print("Sorted (Shellsort): ", a)

print("\nUnsorted (Quicksort): ", b)
q1.quicksort(b, 0, len(b) - 1)
print("Sorted (Quicksort): ", b)

c = q2.merge(a, b)

print("\nLenght of c: ", len(c))
print("\nMerged: ", c)
