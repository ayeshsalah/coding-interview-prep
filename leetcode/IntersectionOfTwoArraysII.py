# Leetcode
# 350. Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        # create counter of the elements in num1
        counts = {}
        for num1 in nums1:
            counts[num1] = counts.get(num1, 0) + 1 # defaults to 0 if new element.
        ##########################################
        ## create counter using collections.Counter
        # counts = collections.Counter(nums1)
        ##########################################
        # check if elements in nums2 are found in nums1
        for num2 in nums2:
            if num2 in counts and counts[num2]>0: 
                #checking if count is > 0 to ensure the same element is not counted twice.
                result.append(num2)
                counts[num2] -= 1 # decrement counter once the element is found in num2
        return result
    