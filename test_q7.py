import answers.q7 as q7

# If you input the following sequence in order:
#
#     12, 34, 13, 56, 9, 11, 7, 5, 3 
# 
# You should getting the following tree.
#
#          56
#        /
#      34
#     /  \
#     |    13
#    /
#  12
#    \
#     |   11
#     \ /
#      9
#       \
#         7
#          \
#            5
#             \
#               3

root = None

while True:
    x = input("Input integer (or anything else to quit): ")

    try:
        x = int(x)

        if root == None:
            root = q7.Node(x)
        else:
            root.add(q7.Node(x))
    except:
        break

    root.draw("", q7.Branch.Root)
