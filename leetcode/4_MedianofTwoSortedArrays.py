# Leetcode
# 4. Median of Two Sorted Arrays
# https://www.youtube.com/watch?v=q6IEA26hvXc


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find smaller of the 2 arrays
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # find total of both arrays
        total = len(nums1) + len(nums2)
        # find half of the 2 arrays. These are the total elements in the left partition.
        mid = total // 2
        
        # run binary search on the smaller array, nums1 in this case.
        left = 0 
        right = len(nums1) - 1
        while True:
            # find middle of the nums1 array 
            nums1_mid = (left + right) // 2
            nums2_mid = mid-nums1_mid-2 # -2 since both arrays are zero indexed.
            # initialize left and right for both arrays.
            # assign default values incase the values go out of bounds. 
            nums1_left = nums1[nums1_mid] if nums1_mid >= 0 else float("-inf")
            nums2_left = nums2[nums2_mid] if nums2_mid >= 0 else float("-inf")
            nums1_right = nums1[nums1_mid+1] if nums1_mid+1 < len(nums1) else float("inf")
            nums2_right = nums2[nums2_mid+1] if nums2_mid+1 < len(nums2) else float("inf")
            # check the partition boundaries 
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # partition is correct
                # check if number of elements are odd, we return 1 value.
                if total % 2:
                    return min(nums1_right, nums2_right)
                # if number of elements are even, we return the average of the 2 values.
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                # move the right index to the left in the nums1 array
                right = nums1_mid - 1
            elif nums2_left > nums1_right:
                # move the left index to the right in the nums1 array 
                left = nums1_mid + 1
