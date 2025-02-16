class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Marks the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create new TrieNode if not found
            node = node.children[char]
        node.is_end_of_word = True  # Mark last node as end of word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word  # True if it's an end of a word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char] 
        return True  # Prefix found
    
    def print_trie(self, node=None, word=''):
        if not node:
            node = self.root
            
        if node.is_end_of_word:
            print(word)
            
        for char, child in node.children.items():
            self.print_trie(child, word + char)

# Usage Example:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # ✅ True
print(trie.search("app"))     # ❌ False
print(trie.startsWith("app")) # ✅ True
trie.insert("app")
print(trie.search("app"))     # ✅ True
trie.print_trie()
