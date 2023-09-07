# Leetcode
# 57. Insert Interval
# https://www.youtube.com/watch?v=A8NUOmlwOlM


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            # check if newInterval is smaller then current interval
            # if it smaller, append to result and return result + remaining valuesof intervals 
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            # check if the newInterval is bigger than the current interval, if yes, append the current interval to result
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
                # not appending to result to check if it overlaps with following intervals
            # if both conditions do not satisify then newInterval is overlapping with current interval
            # update the newInterval, i.e., merge the intervals.
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # not appending to result to check if it overlaps with following intervals
        # if we reach the end of the loop, append the newInterval
        result.append(newInterval)
        return result
