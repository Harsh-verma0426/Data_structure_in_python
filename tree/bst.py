from nodes.tree_node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            return Node(value)
    
        if self.root.data < value:
            self.root.right = self.insert(self.root.right, value)
        elif self.root.data > value:
            self.root.left = self.insert(self.root.left, value)
        
        return self.root

    def find_min(self.):
        current = self.root
        while current and current.left is not None:
            current = current.left
        return current

    def delete(self, value):
        if self.root is None:
            return None
        
        if self.root.data < value:
            self.root.right = self.delete(self.root.right, value)
        elif self.root.data > value:
            self.root.left = self.delete(self.root.left, value)
        else:
            # Node with only one child or no child
            if self.root.left is None:
                return self.root.right
            elif self.root.right is None:
                return self.root.left
            
            # Node with two children: Get the inorder successor
            temp = self.find_min(self.root.right)
            self.root.data = temp.data
            self.root.right = self.delete(self.root.right, temp.data)
            
        return self.root

