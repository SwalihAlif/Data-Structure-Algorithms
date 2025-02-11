class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_to_bt(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            current_node = queue.pop(0)

            if not current_node.left:
                current_node.left = new_node
                return
            else:
                queue.append(current_node.left)

            if not current_node.right:
                current_node.right = new_node
                return
            else:
                queue.append(current_node.right)

    def __is_bst(self, root, min_value, max_value):

        if root is None:
            return None
        
        if not (min_value < root.value < max_value):
            return False
        
        return self.__is_bst(root.left, min_value, root.value) and self.__is_bst(root.right, root.value, max_value)
    
    def is_bst(self):
        return self.__is_bst(self.root, float('-inf'), float('inf'))
    
    def print_bt(self, node=None, level=0, prefix='Root: '):
        if not node:
            node = self.root
            if not node:
                print('Tree is empty.')
                return
            
        if node.right:
            self.print_bt(node.right, level+1, 'R--- ')
        print("   " * level + prefix + str(node.value))
        if node.left:
            self.print_bt(node.left, level+1, 'L--- ')
    
my_tree = BinaryTree()
my_tree.insert_to_bt(10)
my_tree.insert_to_bt(20)
my_tree.insert_to_bt(30)
my_tree.insert_to_bt(40)
my_tree.insert_to_bt(50)
my_tree.insert_to_bt(60)
my_tree.insert_to_bt(70)

my_tree.print_bt()

print(my_tree.is_bst())

    
