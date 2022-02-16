# Leetcode
# 14. Longest Common Prefix


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
        current = self.root
        for alpha in word:           
            if alpha not in current.children:
                current.children[alpha] = TrieNode()
            current = current.children[alpha]
        current.terminal = True
        
    def longest_common_prefix(self):
        current = self.root
        prefix = []
        while len(current.children) == 1 and not current.terminal:
            prefix.append(list(current.children.keys())[0])
            current = current.children[prefix[-1]]
        return "".join(prefix)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Basic idea:
        # Add all words to the trie
        # Then traverse the trie from the root, and we stop when
        #     find a node with more than one child
        #     or
        #     find a node is marked as terminal
        
        # Time: O(n * l) to build the trie
        # n: number of words, l: max length of a word

        trie = Trie()
        for st in strs:
            trie.insert(st)            
        return trie.longest_common_prefix()
