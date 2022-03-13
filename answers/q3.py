# Look on the document for further explanation as to why if there are not
# extreme points the array is sorted.


def extremes(a):
    sorted = True
    ret = []

    for i in range(1, len(a) - 1):
        if (a[i] > a[i + 1] and a[i] > a[i - 1]) or (
            a[i] < a[i + 1] and a[i] < a[i - 1]
        ):
            sorted = False
            print(a[i], end=" ")
            ret.append(a[i])

    if sorted:
        print("SORTED")
    else:
        print()

    return ret
