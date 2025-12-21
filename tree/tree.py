from nodes.tree_node import Node


class Binary_Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)

        else:
            queue = [self.root]
            while queue:
                temp = queue.pop(0)
                if not temp.left:
                    temp.left = Node(value)
                    break
                else:
                    queue.append(temp.left)
                
                if not temp.right:
                    temp.right = Node(value)
                    break
                else:
                    queue.append(temp.right)

    def preorder(self, node):
        if node:
            print(f"{node.value} ", end="")
            self.preorder(node.left)
            self.preorder(node.right)
        else:
            print("Found 0 Nodes in binary tree")


    def inorder(self, node):
        if node:
            self.preorder(node.left)
            print(f"{node.value} ", end="")
            self.preorder(node.right)
        else:
            print("Found 0 Nodes in binary tree")


    def postorder(self, node):
        if node:
            self.preorder(node.left)
            self.preorder(node.right)
            print(f"{node.value} ", end="")
        else:
            print("Found 0 Nodes in binary tree")
