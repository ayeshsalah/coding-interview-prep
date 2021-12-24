# Leetcode
# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/discuss/810795/Python-by-sort-and-merge-w-Visualization

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start index
        intervals.sort(key=lambda x: x[0])
        
        result = []
        
        for interval in intervals:
            # if result is empty OR
            # if end index of previously added interval is less than the first index of the current interval
            # append the interval to result
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            # if end index of previous is greater then start interval of current then 
            # modify the end index of the previous index(i.e. in the result array) with the max of previous and current end index
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
