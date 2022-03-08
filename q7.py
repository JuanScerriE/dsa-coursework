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

    def draw(self, s, parent):
        if self.right != None:
            if parent == Branch.Right or parent == Branch.Root:
                self.right.draw(s[:(len(s) - 1)] + " " + " " * len(str(self.value)) + " |", Branch.Right)
                print(s[:(len(s) - 1)] + " " + " " * len(str(self.value)) + "/")
            else:
                self.right.draw(s[:(len(s) - 1)] + "|" + " " * len(str(self.value)) + " |", Branch.Right)
                print(s[:(len(s) - 1)] + "\\" + " " * len(str(self.value)) + "/")

        print(s[:(len(s) - 1)] + " " + str(self.value))

        if self.left != None:
            if parent == Branch.Left or parent == Branch.Root:
                print(s[:(len(s) - 1)] + " " + " " * len(str(self.value)) + "\\")
                self.left.draw(s[:(len(s) - 1)] + " " + " " * len(str(self.value)) + " |", Branch.Left)
            else:
                print(s[:(len(s) - 1)] + "/" + " " * len(str(self.value)) + "\\")
                self.left.draw(s[:(len(s) - 1)] + "|" + " " * len(str(self.value)) + " |", Branch.Left)


root = Node(7)

root.add(Node(5))
root.add(Node(4))
root.add(Node(6))
root.add(Node(10))
root.add(Node(9))
root.add(Node(8))
root.add(Node(13))
root.add(Node(12))
root.add(Node(-2))
root.add(Node(1))
root.add(Node(34))
root.add(Node(7))
root.add(Node(-42))
root.add(Node(14))
root.add(Node(3))

print(root.get_depth())
print(root.right.depth)

root.draw("", Branch.Root)
