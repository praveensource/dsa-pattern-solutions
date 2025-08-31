"""
Problem: Longest Consecutive Sequence
------------------------------------
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)  # O(1) lookups
        longest = 0

        for num in num_set:
            # Only start counting if this is the start of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1

                while current + 1 in num_set:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest


# ✅ Example Run
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))   # Output: 4
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # Output: 9
    print(sol.longestConsecutive([1,0,1,2]))           # Output: 3
