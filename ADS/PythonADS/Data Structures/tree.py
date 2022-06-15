# TREES
# BINARY TREE
# each node is greater than every node in it's left subtree
# each node is less than every node in it's right subtree
# Operations: insert(), find(), delete(), get_size(), traversals
# insert(), find(), delete() are O(log n)
# Inserts start at the root (at the top of the tree) and then "bubble down"
class Tree:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True
    
    def find(self, data):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                self.right.find(data)

    def delete(self, data):
        pass
    
    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1
    
    def preorder(self):
        if self is not None:
            print(self.data, end=' ')
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()
    
    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.inorder()
            
# tree = Tree(7)
# tree.insert(9)
# for i in [15, 10, 2, 12, 3, 1, 13, 6, 11, 4, 14, 9]:
#     tree.insert(i)

# for i in range(16):
#     print(tree.find(i), end=' ')
# print('\n', tree.get_size())

# tree.preorder()
# print()
# tree.inorder()
# print()
