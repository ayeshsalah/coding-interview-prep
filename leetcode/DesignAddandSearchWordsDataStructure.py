# Leetcode
# 211. Design Add and Search Words Data Structure
# Builds on Leetcode #208
# https://www.youtube.com/watch?v=BTf05gs_8iU


class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False
        

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        current = self.root
        for alpha in word:
            if alpha not in current.children:
                current.children[alpha] = TrieNode()
            current = current.children[alpha]
        current.terminal = True

    def search(self, word: str) -> bool:
        # call dfs recursively if alphabet is "." else check iteratively 
        def dfs(index, node):
            current = node
            for i in range(index, len(word)):
                alpha = word[i]
                if alpha == ".":
                    for child in current.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if alpha not in current.children:
                        return False
                    current = current.children[alpha]
            return current.terminal

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
