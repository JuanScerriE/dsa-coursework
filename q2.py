def merge(a, b):
    c = []

    for e in a:
        c.append(e)

    for e in b:
        c.append(e)
    
    return c

vec_a = [1,2,3,4,5,6,7,8,9]
vec_b = [10,11,12,13,14,15,16,17,18]

vec_c = merge(vec_a, vec_b)

print(vec_c)
