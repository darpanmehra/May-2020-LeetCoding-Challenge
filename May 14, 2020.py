#208. Implement Trie (Prefix Tree)
#Implement a trie with insert, search, and startsWith methods.
#Example:
#Trie trie = new Trie();
#trie.insert("apple");
#trie.search("apple");   // returns true
#trie.search("app");     // returns false
#trie.startsWith("app"); // returns true
#trie.insert("app");
#trie.search("app");     // returns true

class TrieNode:
    def __init__(self):
        self.endofWord = False
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endofWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.endofWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True