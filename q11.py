import math

def sin(x):
    while x < -math.pi or x > math.pi:
        if x >= 0:
            x -= 2*math.pi
        else:
            x += 2*math.pi

    return x - (x**3)/6 + (x**5)/120 - (x**7)/5040 + (x**9)/362880 - (x**11)/39916800 + (x**13)/6227020800

def cos(x):
    return sin(x + math.pi/2)


print("Sine Test (In Radians)\n")

print("sin(45) = " + str(sin(45)))
print("sin(12) = " + str(sin(12)))
print("sin(0.5) = " + str(sin(0.5)))
print("sin(0) = " + str(sin(0)))

print("\nCosine Test (In Radians)\n")

print("cos(-13) = " + str(cos(-13)))
print("cos(pi) = " + str(cos(math.pi)))
print("cos(1.2345) = " + str(cos(1.2345)))
print("cos(45) = " + str(cos(45)))
