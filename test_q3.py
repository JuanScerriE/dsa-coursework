import answers.q1 as q1
import answers.q3 as q3
import random

print("Extremes Test\n")

if [5, 3, 8, 7, 15] == q3.extremes([0, 5, 3, 6, 8, 7, 15, 9]):
    print("Test Passed")
else:
    print("Test Failed")

if [] == q3.extremes([0, 3, 5, 6, 7, 8, 9, 15]):
    print("Test Passed\n")
else:
    print("Test Failed\n")

a = []

len_a = random.randint(4, 16)

# Populate a with random integers.
for i in range(len_a):
    a.append(random.randint(0, 32))

print("Unsorted (Shellsort): ", a)
print("\nChecking for extremes before sort...")
q3.extremes(a)

q1.shellsort(a)

print("\nSorted (Shellsort): ", a)
print("\nChecking for extremes after sort...")
q3.extremes(a)
