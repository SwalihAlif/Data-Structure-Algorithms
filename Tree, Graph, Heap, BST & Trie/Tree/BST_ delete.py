class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
        
# bst.r_insert(10)
# bst.r_insert(5)
# bst.r_insert(15)
# bst.r_insert(3)
# bst.r_insert(7)
# bst.r_insert(11)
# bst.r_insert(17)
# bst.r_insert(17)
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
        
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
        
    def __delete_node(self, current_node, value):
        if current_node == None:
            return None # Base case: If the node is not found
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            # Node found - Now handle deletion
            if current_node.left == None and current_node.right == None:
                return None # Case 1: leaf node (no children), simply remove it
            elif current_node.left == None:
                current_node = current_node.right # Case 2: Only right child exists, replace node with right child
            elif current_node.right == None:
                current_node = current_node.left # Case 2: Only left child exists, replace node with left child
            else:
                sub_tree_min = self.min_value(current_node.right) # Case 3: Node has two children, find successor
                current_node.value = sub_tree_min # Replace value with inorder successor
                current_node.right = self.__delete_node(current_node.right, sub_tree_min) # Delete the successor node
                
        return current_node # return the modified tree
        
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value) # Start the deletion from the root
        
            
        
    def print_bst(self):
        def normal_print(node):
            if node:
                normal_print(node.left)
                print(node.value, end=' ')
                normal_print(node.right)
        if self.root is None:
            print('Tree is empty.')
        else:
            normal_print(self.root)
            print()
    def print_bst_visual(self, node=None, level=0, prefix='Root: '):
        if node is None:
            node = self.root
            if node is None:
                print("Tree is empty.")
                return
        if node.right:
            self.print_bst_visual(node.right, level +1, 'R-- ')
        print("  " * level + prefix + str(node.value))
        if node.left:
            self.print_bst_visual(node.left, level + 1, 'L-- ')

bst = BinarySearchTree()
bst.r_insert(10)
bst.r_insert(5)
bst.r_insert(15)
bst.r_insert(3)
bst.r_insert(7)
bst.r_insert(11)
bst.r_insert(17)
bst.r_insert(17)

bst.print_bst()
print('------------------------------------------------')
bst.print_bst_visual()
print('------------------------------------------------')
print(bst.min_value(bst.root))
print('------------------------------------------------')
bst.delete_node(10)
bst.print_bst_visual()