class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


root = Tree()
root.data = 0
root.left = Tree()
root.left.data = 1
root.right = Tree()
root.right.data = 2

# print(root.data)
