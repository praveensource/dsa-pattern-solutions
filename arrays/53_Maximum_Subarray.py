from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize both current and max sum with the first element
        current_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            # Either extend the subarray or start fresh at nums[i]
            current_sum = max(nums[i], current_sum + nums[i])
            # Update global max
            max_sum = max(max_sum, current_sum)

        return max_sum


"""
Time Complexity: O(n)  -> single pass
Space Complexity: O(1) -> only two variables
"""
