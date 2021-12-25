# Leetcode
# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/discuss/622135/Two-simple-Python-solutions-with-explanation


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals by end index
        intervals.sort(key=lambda x: x[1])
        
        previous = float("-inf")
        count = 0
        
        for interval in intervals:
            # store end index in previous
            # if current start index is greater than previous end index, then update the previous with current end index.
            if interval[0] >= previous:
                previous = interval[1]
            # current start is smaller than previous end, increment counter.
            # when sorted by end time and if overlap occurs, the interval that comes later must be the one to remove as it has larger end time. 
            else:
                count +=1 
        return count
