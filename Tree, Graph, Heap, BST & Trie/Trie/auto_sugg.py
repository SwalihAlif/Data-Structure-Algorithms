class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def suggest(self, prefix):
        def dfs(node, path, results):
            if node.is_end_of_word:
                results.append(path)
            for char, next_node in node.children.items():
                dfs(next_node, path + char, results)
        
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        suggestions = []
        dfs(current, prefix, suggestions)
        return suggestions
    
    def print_trie(self, node=None, prefix='', indent=''):
        if node is None:
            node = self.root

        for char, child_node in sorted(node.children.items()):
            is_end = '(is_end_of_word = True)' if child_node.is_end_of_word else ''
            print(f"{indent}- '{char}' {is_end}")
            self.print_trie(child_node, prefix + char, indent + '    ') 


words = ['cat', 'car', 'cap', 'dog', 'doll', 'dot', 'can']

trie = Trie()
for word in words:
    trie.insert(word)

print("root")
trie.print_trie()
