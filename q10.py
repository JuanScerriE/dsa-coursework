# This is a very compact recursive algorithm for finding the maximum inspired
# by merge sort. The first implementation `max` returns a singleton with
# the largest element of the provided list. However, it has
# three recursive calls instead of 2.

# `max_2` is similar to `max` if just eliminates the need for the third
# recursive call.

def max(list):
    if len(list) == 1:
        return [list[0]]
    elif len(list) == 2:
        return [list[0]] if list[0] > list[1] else [list[1]]
    else:
        return max(max(list[:len(list)//2]) + max(list[len(list)//2:]))


def half(list):
    return list[:len(list)//2], list[len(list)//2:]

def max_2(list):
    if len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        list_u, list_l = half(list)

        u = max_2(list_u)
        l = max_2(list_l)

        return u if u > l else l


print("`max` Implementation\n")

print("max([13,14,1,3,7,5,21,59]) = " + str(max([13,14,1,3,7,5,21,59])))
print("max([88,14,1,3,7,21,59]) = " + str(max([88,14,1,3,7,21,59])))
print("max([13,-1214,1,3,7,5,21,59]) = " + str(max([13,-1214,1,3,7,5,21,59])))
print("max([13,14,1,12,34,123,3,7,5,21,59]) = " + str(max([13,14,1,12,34,123,3,7,5,21,59])))

print("\n`max_2` Implementation\n")

print("max_2([13,14,1,3,7,5,21,59]) = " + str(max_2([13,14,1,3,7,5,21,59])))
print("max_2([88,14,1,3,7,21,59]) = " + str(max_2([88,14,1,3,7,21,59])))
print("max_2([13,-1214,1,3,7,5,21,59]) = " + str(max_2([13,-1214,1,3,7,5,21,59])))
print("max_2([13,14,1,12,34,123,3,7,5,21,59]) = " + str(max_2([13,14,1,12,34,123,3,7,5,21,59])))
