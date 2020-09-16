from binarytree import build


class Tree:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def min_node_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Delete node from the tree
    def delete_node(self, root, data):
        # check if the tree is empty
        if root is None:
            return root

        # check if the key is smaller than root key, if so it is in left subtree
        if data < root.data:
            root.left = root.delete_node(root.left, data)

        # check if the key is larger than root key, if so it is in right subtree
        elif data > root.data:
            root.right = root.delete_node(root.right,data)

        # else the key is the root key
        # three types of deletions : a.leaf node  b.node has one child  c.node has two children
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # get the right subtree smallest value
            node = temp.minNodeValue(root.right)

            # replace root key with inoeder success key
            root.data = node.key

            # delete right successor node
            root.right.delete_node(root.right,node.key)
        return root

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print( self.data),
        if self.right:
            self.right.print_tree()

    # def printNode(self,root):
    #     root.dislayTree(root,0)

# Use the insert method to add nodes

root = Tree(12)
root.insert(6)
root.insert(14)
root.insert(3)
# root.minNodeValue(root)

root.print_tree()

root.delete_node(root,14)
root.print_tree()

# List of nodes 
nodes =[56, 6, 8, 24, 11, None, 13]
  
# Building the binary tree
binary_tree = build(nodes)
print('Binary tree from list :\n',
      binary_tree) 
  
# Getting list of nodes from binary tree
print('\nList from binary tree :',  
      binary_tree.values) 

