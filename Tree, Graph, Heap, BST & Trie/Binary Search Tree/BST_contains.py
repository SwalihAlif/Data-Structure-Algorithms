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
                print("Tree is empty")
                return
        if node.right:
            self.print_bst_visual(node.right, level +1, 'R--- ')
        print("  " * level + prefix + str(node.value))
        if node.left:
            self.print_bst_visual(node.left, level+1, 'L--- ')

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
bst.print_bst_visual()

print(bst.r_contains(17))
print(bst.r_contains(173))
        