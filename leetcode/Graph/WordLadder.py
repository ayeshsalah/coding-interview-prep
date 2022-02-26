# Leetcode
# 127. Word Ladder
# https://www.youtube.com/watch?v=h9iTnkgv05E


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # add the beginWord to wordList
        wordList.append(beginWord)
        
        # build adjacency list based on patterns
        adjacency_list = collections.defaultdict(list) # creates a default list for every key
        for word in wordList:
            for i in range(len(word)):
                # build patterns by replacing every char with a *
                pattern = word[:i] + "*" + word[i+1:]
                adjacency_list[pattern].append(word)
                
        # run BFS to find shortest path
        visited = set([beginWord])
        queue = deque([beginWord])
        result = 1
        while queue:
            for k in range(len(queue)):
                word = queue.popleft()
                # if current word is endWord return result
                if word == endWord:
                    return result
                for i in range(len(word)):
                    # build patterns by replacing every char with a *
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbour in adjacency_list[pattern]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
            result += 1
        return 0
