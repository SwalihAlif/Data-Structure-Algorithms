class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert_bt(self, value):
        new_node = Node(value)
        
        if not self.root:
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
            
    def print_bt(self, node=None, level=0, prefix="Root: "):
        
        if node is None:
            node = self.root
            if not node:
                print("The tree is empty...")
                return
            
        if node.right:
            self.print_bt(node.right, level+1, "R---")
        print("   " * level + prefix + str(node.value))
        if node.left:
            self.print_bt(node.left, level+1, "L---")

    def get_height(self, node=None):
        if not node:
            return -1
            
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return 1 + max(left_height, right_height)
            
            
bt = BinaryTree()
bt.insert_bt(10)
bt.insert_bt(10)
bt.insert_bt(10)
bt.insert_bt(20)
bt.print_bt()
print(bt.get_height(bt.root))