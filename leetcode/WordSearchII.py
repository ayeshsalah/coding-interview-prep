# Leetcode
# 212. Word Search II
# https://www.youtube.com/watch?v=asbcE9mZz_U
# 2 optimizations on the solution in the video 
# 1. whenever you add a word, you can set the terminal to False, then can set result as a list. This should avoid adding the same word twice. 
# 2. visit is not needed, set the board value to None before going to the next depth
# https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).


class Trie:
    def __init__(self):
        self.children = {}
        self.terminal = False
        
    def add_word(self, word):
        current = self
        
        for alpha in word:
            if not current.children.get(alpha):
                current.children[alpha] = Trie()
            current = current.children.get(alpha)
        current.terminal = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        # create trie with all the words in the list
        for word in words:
            root.add_word(word)
        
        rows = len(board)
        cols = len(board[0])
        result = []
        visiting = set()
        
        def dfs(row, col, current_node, word):
            # failure case
            if (row < 0 or col < 0 or 
                row >= rows or col >= cols or
                (row, col) in visiting or
                board[row][col] not in current_node.children):
                return 
            
            temp = board[row][col]
            
            current_node = current_node.children.get(board[row][col])
            word += board[row][col]
            # base case
            if current_node.terminal:
                result.append(word)
                current_node.terminal = False

            board[row][col] = None
            dfs(row+1, col, current_node, word)
            dfs(row-1, col, current_node, word)
            dfs(row, col+1, current_node, word)
            dfs(row, col-1, current_node, word)
            board[row][col] = temp
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")
        return list(result)
