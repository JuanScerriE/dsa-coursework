# So, this algorithm makes use of the properties of the builtin Python
# dictionary type (which is constructed off of a hash table). The idea is that
# I will loop over all the elements of a list once indexing every element in
# the dictionary. If the dictionary already contains the element, the algorithm
# will increase the count otherwise it will add the new element to the
# dictionary. This means that we are looping over the list once to count how
# many times each unique element occurs.

# So, we are creating a dictionary whose space-complexity is generally O(n) in
# the worst case. And in the average case the time-complexity is generally
# O(1). Which means that we have a O(n) time-complexity algorithm for counting
# the number of occurences of every unique number. Then we are again creating
# an array which can have a worst case space-complexity of O(n). And we are
# looping over the dictionary again which is an operation with time complexity
# O(n).abs

# Therefore, the average time-complexity is O(2n) and the worst case space
# complexity is O(2n). And since O(2n) = O(n). The algorithm has an average
# time-complexity of O(n). However, this is only for the average case.

# To ensure the best worse case scenario we should implement an efficient
# sorting algorithm which can allow us to cap the algorithm at a worst case
# of O(n lgon n).

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
