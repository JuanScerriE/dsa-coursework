from random import randint

def product_relation(S):
    M = set()

    for a in S:
        for b in S.difference({a}):
            for c in S.difference({a,b}):
                for d in S.difference({a,b,c}):
                    if a*b == c*d:
                        M.add(((a, b), (c, d)))
                        # M.add(frozenset([a, b, c, d]))

    return M

T = set()

for i in range(32):
    T.add(randint(1, 1024))

print(T)

R = product_relation(T)

for r in R:
    print(r)
