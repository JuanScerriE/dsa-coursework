from enum import Enum


class Branch(Enum):
    Left = 0
    Root = 1
    Right = 2


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, node):
        if node.value > self.value:
            if self.right == None:
                self.right = node
            else:
                self.right.add(node)
        else:
            if self.left == None:
                self.left = node
            else:
                self.left.add(node)

    # I need to explain this algorithm otherwise I will forget what I am doing.
    # So basically, I arrived at this algorithm by a process of convergence and
    # experimentation I was not sure if I could do this But I realised that
    # instead of for example passing the number of spaces for padding as a
    # parameter to draw() we can just pass the string to pad with. This gives
    # us a lot of control. Effectively, if we branch to the right we want to
    # first draw the rest of the branch and then draw our element so the tree
    # is balanced. The final character of our padding is `|` this allows us to
    # create the connection. However, after two successive right draws the '|'
    # must be removed and a new one should be added. The same goes for two
    # successive lefts. If we have a right and left or a left and a right we
    # keep the pipe where it is because that would be in the inner part of the
    # tree. This is what the parent parameter is for. I think that is the gist.
    # I should be able to remember it.

    def draw(self, s, parent):
        if self.right != None:
            if parent == Branch.Right or parent == Branch.Root:
                self.right.draw(
                    s[: (len(s) - 1)] + " " + " " * len(str(self.value)) + " |",
                    Branch.Right,
                )
                print(s[: (len(s) - 1)] + " " + " " * len(str(self.value)) + "/")
            else:
                self.right.draw(
                    s[: (len(s) - 1)] + "|" + " " * len(str(self.value)) + " |",
                    Branch.Right,
                )
                print(s[: (len(s) - 1)] + "\\" + " " * len(str(self.value)) + "/")

        print(s[: (len(s) - 1)] + " " + str(self.value))

        if self.left != None:
            if parent == Branch.Left or parent == Branch.Root:
                print(s[: (len(s) - 1)] + " " + " " * len(str(self.value)) + "\\")
                self.left.draw(
                    s[: (len(s) - 1)] + " " + " " * len(str(self.value)) + " |",
                    Branch.Left,
                )
            else:
                print(s[: (len(s) - 1)] + "/" + " " * len(str(self.value)) + "\\")
                self.left.draw(
                    s[: (len(s) - 1)] + "|" + " " * len(str(self.value)) + " |",
                    Branch.Left,
                )
