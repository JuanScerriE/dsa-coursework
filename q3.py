# Look on the document for further explanation as to why if there are not
# extreme points the array is sorted.

def extremes(a):
    sorted = True

    for i in range(1, len(a) - 1):
        if (a[i] > a[i + 1] and a[i] > a[i - 1]) or (a[i] < a[i + 1] and a[i] < a[i - 1]):
            sorted = False
            print(a[i],end=" ")

    if sorted:
        print("SORTED")
    else:
        print()


extremes([0,5,3,6,8,7,15,9])
extremes([0,3,5,6,7,8,9,15])
