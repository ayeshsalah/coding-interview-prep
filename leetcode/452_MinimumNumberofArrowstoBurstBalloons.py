# Leetcode
# 452. Minimum Number of Arrows to Burst Balloons
# Similar to 56. Merge Intervals


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        overlap = []
        points = sorted(points, key=lambda x:x[0])
        for item in points:
            if not overlap or overlap[-1][1]<item[0]:
                overlap.append(item)
            else:
                prev_start, prev_end = overlap.pop()
                overlap.append([max(prev_start, item[0]), min(prev_end, item[1])])
        return len(overlap)
