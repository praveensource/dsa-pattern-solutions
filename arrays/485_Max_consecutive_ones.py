from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Problem:
	Link --> https://leetcode.com/problems/max-consecutive-ones/
        Given a binary array nums (containing only 0s and 1s),
        return the maximum number of consecutive 1s in the array.
        
        Example:
        nums = [1,1,0,1,1,1] → Output = 3
	TC, SC = O(N), O(1)
        """

        # current_count → tracks current streak of consecutive 1s
        # max_count → stores the maximum streak seen so far
        current_count = 0
        max_count = 0

        # Traverse the array
        for num in nums:
            if num == 1:
                # Extend the current streak of 1s
                current_count += 1
                # Update maximum streak if current is greater
                max_count = max(max_count, current_count)
            else:
                # Streak breaks when we see a 0 → reset counter
                current_count = 0
        
        # Answer = maximum streak found
        return max_count
