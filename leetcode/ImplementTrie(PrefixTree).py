# Leetcode
# 208. Implement Trie (Prefix Tree)
# https://www.youtube.com/watch?v=oobqoCJlHA0


class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # if alpha exists in children dict, move the current to next node
        # if alpha does not exists, add TrieNode to children dict and move the current to next node
        # code can be shortened, it is simplistic to enable easy understanding later.         
        current = self.root
        for alpha in word:           
            if current.children.get(alpha):
                current = current.children.get(alpha)
            else:
                current.children[alpha] = TrieNode()
                current = current.children.get(alpha)
        current.terminal = True

    def search(self, word: str) -> bool:
        # if alpha does not exists in children return False
        # if alpha exists and end of loop is reached, then return terminal value.
        # terminal will be False if only part of the word is being searched. 
        current = self.root
        for alpha in word:
            if current.children.get(alpha):
                current = current.children.get(alpha)
            else:
                return False
        return current.terminal

    def startsWith(self, prefix: str) -> bool:
        # if alpha does not exists in children return False
        # if alpha exists and end of loop is reached, then return True as we do not have to check for end of the word.
        current = self.root
        for alpha in prefix:
            if current.children.get(alpha):
                current = current.children.get(alpha)
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)