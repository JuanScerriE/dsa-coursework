# This algorithm makes use of the properties of the builtin
# Python dictionary type (which is constructed off of a hash
# table).
#
# The idea: We loop over all the elements of an array once
# indexing every element in the dictionary.
#
# If the dictionary already contains the element, the algorithm
# will increase the count otherwise it will add the new element
# to the dictionary. This means that we are looping over the
# list once to count how many times each unique element occurs.

# We are creating a dictionary whose worst case space-complexity
# is O(n). Moreover, the average case time-complexity is of the
# dictionary is O(1).
#
# This means that our algorithm has an average time-complexity
# of O(2n) since we are looping over each element twice. Once to
# index them in the dictionary and the other time to check which
# ones have duplicates. 
# 
# Moreover, the space-complexity of our algorithm is also O(2n)
# since we are creating a second array to hold all the values
# which had duplicates apart from the space-complexity of the
# dictionary.

def find_dups(list):
    dict = {}

    for i in range(len(list)):
        if dict.get(list[i], 0) == 0:
            dict[list[i]] = 1
        else:
            dict[list[i]] += 1

    dups = []

    for key in dict:
        if dict[key] != 1:
            dups.append(key)

    return dups
