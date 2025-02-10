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

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def longest_prefix(self):
        current = self.root
        prefix = ""
        while len(current.children) == 1 and not current.is_end_of_word:
            char = next(iter(current.children))
            prefix += char
            current = current.children[char]
        return prefix

    def count_word_with_prefix(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        return self._count_word(current)

    def _count_word(self, node):
        count = 1 if node.is_end_of_word else 0
        for char in node.children:
            count += self._count_word(node.children[char])
        return count

    def get_words(self, node=None, prefix=""):
        if node is None:
            node = self.root
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self.get_words(child_node, prefix + char))
        return words

    def display(self, node=None, prefix="", is_last=True, indent=""):
        if node is None:
            node = self.root

        if node is not self.root:
            print(indent + ("└── " if is_last else "├── ") + prefix + (" (isEndOfWord: true)" if node.is_end_of_word else ""))
            indent += "    " if is_last else "│   "

        children_keys = list(node.children.keys())
        for index, key in enumerate(children_keys):
            is_last_child = index == len(children_keys) - 1
            self.display(node.children[key], key, is_last_child, indent)


# Example Usage:
trie = Trie()

trie.insert('intern')
trie.insert('diog')
trie.insert('r')
trie.insert('zog')
trie.insert('internet')
trie.insert('interview')
trie.insert('interview')
trie.insert('instagram')

print(trie.get_words())
print(trie.starts_with('in'))
print(trie.longest_prefix())

# Display the Trie Structure
# trie.display()
