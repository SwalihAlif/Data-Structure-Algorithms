class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
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

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
    def r_contains(self, value):
        return self.__r_contains(self.root, value)

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
        
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self): 
        results = []
        
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
        
    def dfs_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
        
    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results 
        
    def print_bst(self):
        def normal_print(node):
            if node:
                normal_print(node.left)
                print(node.value, end=' ')
                normal_print(node.right)
        if self.root is None:
            print("Tree is empty.")
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
            self.print_bst_visual(node.right, level+1, 'R--- ')
        print("  " * level + prefix + str(node.value))
        if node.left:
            self.print_bst_visual(node.left, level+1, 'L--- ')

    def __is_bst(self, root, min_value, max_value):

        if root is None:
            return True
        
        if not (min_value < root.value < max_value):
            return False
        
        return self.__is_bst(root.left, min_value, root.value) and self.__is_bst(root.right, root.value, max_value)
    def is_bst(self):
        return self.__is_bst(self.root, float('-inf'), float('inf'))

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
print(bst.BFS())
print('------------------------------------------------')
print('dfs pre order:', bst.dfs_pre_order())
print('------------------------------------------------')
print('dfs post order:', bst.dfs_post_order())
print('------------------------------------------------')
print('dfs post order:', bst.dfs_in_order())
print('------------------------------------------------')
print('Is it a BST: ', bst.is_bst())
print('------------------------------------------------')
