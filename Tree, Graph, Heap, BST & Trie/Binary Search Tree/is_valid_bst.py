class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        self.__r_insert(self.root, value)
    
    def print_bst(self, node=None, level=0, prefix='Root: '):
        if not node:
            node = self.root
            if not node:
                print('Tree is empty.')
                return
        if node.right:
            self.print_bst(node.right, level+1, 'R---')
        print("   " * level + prefix + str(node.value))
        if node.left:
            self.print_bst(node.left, level+1, 'L---')
            
    def __is_bst(self, root, min_value, max_value):
        if not root:
            return True
        if not (min_value < root.value < max_value):
            return False
        return self.__is_bst(root.left, min_value, root.value) and self.__is_bst(root.right, root.value, max_value)
    def is_bst(self):
        return self.__is_bst(self.root, float('-inf'), float('inf'))
        
my_tree = BinarySearchTree()
my_tree.insert(3)
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(4)
my_tree.insert(5)
my_tree.print_bst()
print('It is BST: ', my_tree.is_bst())