# Leetcode
# 39. Combination Sum
# https://www.youtube.com/watch?v=GBKI9VSKdGg
# https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # dfs backtracking approach
        # 2 decisions 
        # 1. Add the current element to the total
        # 2. Do not add the current element
        result = []
        def dfs(i, current, total):
            if total == target:
                result.append(current.copy())
                return
            if total>target or i>=len(candidates):
                return
            # adding current element
            current.append(candidates[i])
            dfs(i, current, total+candidates[i])
            # not adding the curernt element          
            current.pop()
            dfs(i+1, current, total)
            
        dfs(0, [], 0)
        return result


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # another dfs backtracking approach 
        # subtract the current element from the target, instead of adding and maintaining a total
        # append path to result when target is 0 
        # if target goes below 0, return 
        # when base conditions are not met, 
        # 1. subtract the element from the target, 
        # 2. add the element to list of the visited element, i.e., path
        # ensure the path value is a new object, if the reference is passed the answer will be incorrect.
        result = []
        self.dfs(candidates, target, [], result)
        return result
    
    def dfs(self, array, target, path, result):
        if target == 0:
            result.append(path)
            return
        if target < 0 :
            return
        for i in range(len(array)):
            # print(array[i:])
            # print("target:", target)
            # print("path: ", path)
            self.dfs(array[i:], target-array[i], path+[array[i]], result)