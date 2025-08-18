from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Problem:
        Given an integer array nums, return True if it is possible to obtain a 
        non-decreasing sorted array by rotating nums. Otherwise, return False.
        
        Example: [3,4,5,1,2] -> True (rotation of [1,2,3,4,5])
        """

        pairs = 0               # Count how many "descending pairs" exist
        n = len(nums)

        # Step 1: Traverse array and count descending pairs
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                pairs += 1
        
        # Step 2: Check wrap-around pair (last element vs first element)
        if nums[n - 1] > nums[0]:
            pairs += 1
        
        # Step 3: Array is sorted & rotated if at most ONE descending pair exists
        return pairs <= 1
