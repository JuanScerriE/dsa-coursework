from enum import Enum

class Branch(Enum):
    Left = 0
    Root = 1
    Right = 2

class Node:
    def __init__(self, value):
        self.value = value
        self.depth = 1
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

    def get_depth(self):
        if self.left != None and self.right != None:
            left_depth = self.left.get_depth()
            right_depth = self.right.get_depth()

            self.depth += left_depth if left_depth > right_depth else right_depth
        
        if self.left != None and self.right == None:
            self.depth += self.left.get_depth()

        if self.left == None and self.right != None:
            self.depth += self.right.get_depth()

        return self.depth

    def draw(self, s, parent):
        if self.right != None:
            m_s = s[:(len(s) - 1)]
            if parent == Branch.Right or parent == Branch.Root:
                m_s += " " + " " * len(str(self.value))
            else:
                m_s += "|" + " " * len(str(self.value))

            self.right.draw(m_s + " |", Branch.Right)
            print(m_s + "/")

        print(s[:(len(s) - 1)] + " " + str(self.value))

        if self.left != None:
            m_s = s[:(len(s) - 1)]
            if parent == Branch.Left or parent == Branch.Root:
                m_s += " " + " " * len(str(self.value))
            else:
                m_s += "|" + " " * len(str(self.value))

            print(m_s + "\\")
            self.left.draw(m_s + " |", Branch.Left)


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
