from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        
        if n < 4:  # Handle edge case
            return []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates
                    continue

                k = j + 1
                l = n - 1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        # Skip duplicates after finding a valid quadruplet
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

                    elif total < target:
                        k += 1
                    else:
                        l -= 1
        return ans