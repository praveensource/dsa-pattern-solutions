from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # count -> tracks length of current consecutive zero streak
        # total -> total number of zero-filled subarrays
        count = 0
        total = 0

        for num in nums:
            if num == 0:
                count += 1
                # each new zero adds 'count' new subarrays
                total += count
            else:
                # reset count when a nonzero is found
                count = 0

        return total


"""
Time Complexity: O(n)  -> we scan the array once
Space Complexity: O(1) -> only counters used
"""
