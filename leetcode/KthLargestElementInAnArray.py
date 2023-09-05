# Leetcode
# 215. Kth Largest Element in an Array
# https://www.youtube.com/watch?v=XEmy13g1Qxc

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using quick select
        # make the k the index we are looking for in the final result.
        k = len(nums)-k
        return self.quick_select(nums, k, 0, len(nums)-1)
        
    def quick_select(self, nums, k, left, right):
        pivot = nums[right] # choosing the right most value as pivot
        pointer = left
        # since range is not inclusive of the right element, this works. We do not want to include the right element.
        for i in range(left, right):
            # if the nums[i](current element) is less then pivot then swap the current element with nums[pointer] 
            # and increment pointer. 
            if nums[i] <= pivot:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer +=1
        # swap last element (pivot in this case) with the pointer.
        nums[pointer], nums[right] = nums[right], nums[pointer]
        # if pointer is less than the target index, search in the left sub array 
        # if pointer is greater then the target index, search in the right sub array 
        # if pointer is equal to target index, return the number at the target index.
        if pointer > k:
            return self.quick_select(nums, k, left, pointer-1 )
        elif pointer < k:
            return self.quick_select(nums, k, pointer+1, right)
        else:
            return nums[pointer]

#################################################################


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
