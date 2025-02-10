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
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
        
    def print_bst_visual(self, node=None, level=0, prefix='Root: '):
        if node is None:
            node = self.root
            if node is None:
                print('Tree is empty.')
                return
        if node.right:
            self.print_bst_visual(node.right, level+1, 'R--- ')
        print("  " * level + prefix + str(node.value))
        if node.left:
            self.print_bst_visual(node.left, level+1, 'L--- ')
            
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
        while current_node.left:
            current_node = current_node.left
        return current_node.value
    
    def __delete_node(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            return self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                subtree_min = self.min_value(current_node.right)
                current_node.value = subtree_min
                current_node.right = self.__delete_node(current_node.right, subtree_min)
        return current_node
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)

my_tree = BinarySearchTree()
my_tree.r_insert(30)
my_tree.r_insert(20)
my_tree.r_insert(10)
my_tree.r_insert(40)
my_tree.r_insert(50)
my_tree.print_bst_visual()
print(my_tree.r_contains(50))
my_tree.delete_node(30)
my_tree.print_bst_visual()
