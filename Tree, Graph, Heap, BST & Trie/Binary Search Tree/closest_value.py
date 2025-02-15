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
    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
        
    def print_bst(self, node=None, level=0, prefix='Root: '):
        if not node:
            node = self.root
            if not node:
                print('Tree is empty.')
                return 
        if node.right:
            self.print_bst(node.right, level+1, 'R--- ')
        print("   " * level + prefix + str(node.value))
        if node.left:
            self.print_bst(node.left, level+1, 'L--- ')
        
    def find_closest_value(self, root, target):
        if not self.root:
            return None
            
        def dfs(node, closest):
            if not node:
                return closest
                
            if abs(node.value - target) < abs(closest - target):
                closest = node.value
            
            if target < node.value:
                return dfs(node.left, closest)
            else:
                return dfs(node.right, closest)
        return dfs(self.root, self.root.value)
        
        
my_bst = BinarySearchTree()
values = [30, 20, 10, 40, 50]

for i in values:
    my_bst.r_insert(i)
    
my_bst.print_bst()

targets = [6, 17, 39, 28, 60]

for t in targets:
    closest = my_bst.find_closest_value(my_bst.root, t)
    print(f"The closest value to {t} is {closest}")