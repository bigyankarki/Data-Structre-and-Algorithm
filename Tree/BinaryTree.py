class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self, root):
        self.rootNode = Node(root)
        self.root = self.rootNode.data

    def insert_left(self, data):
        if self.rootNode.left is None:
            self.rootNode.left = Binary_Tree(data)

    def insert_right(self, data):
        if self.rootNode.right is None:
            self.rootNode.right = Binary_Tree(data)

    def get_left_element(self):
        node = self.rootNode.left
        return node.root

    def get_right_element(self):
        node = self.rootNode.right
        return node.root


bt = Binary_Tree(0)
bt.insert_left(1)
bt.insert_right(2)

bt.rootNode.left.insert_left(3)
bt.rootNode.left.insert_right(4)

bt.rootNode.right.insert_left(5)
bt.rootNode.right.insert_right(6)

print("Root Node:", bt.root)
print("Left element from root node:", bt.get_left_element())
print("Right element from root node:", bt.get_right_element())

print("Leftmost element from the root:", bt.rootNode.left.get_left_element())
print("Rightmost element from the left node of the root:", bt.rootNode.left.get_right_element())
print("Leftmost element from the right node of the root:", bt.rootNode.right.get_left_element())
print("Rightmost element from the root:", bt.rootNode.right.get_right_element())