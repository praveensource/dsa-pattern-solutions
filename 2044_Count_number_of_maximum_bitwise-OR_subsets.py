# Problem: Count the number of subsets with maximum bitwise OR
# Approach: Use DFS (backtracking) to explore all possible non-empty subsets
# and keep track of the number of subsets that give the maximum OR.

from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Initialize the variables to track max OR value and the count of subsets
        self.max_or = 0
        self.count = 0

        # Helper function to perform DFS
        def dfs(index: int, curr_or: int):
            # If we have considered all elements
            if index == len(nums):
                # If current OR is equal to the max OR seen so far
                if curr_or == self.max_or:
                    self.count += 1
                # If we found a new max OR, update and reset count
                elif curr_or > self.max_or:
                    self.max_or = curr_or
                    self.count = 1
                return

            # Include current element in subset
            dfs(index + 1, curr_or | nums[index])
            # Exclude current element from subset
            dfs(index + 1, curr_or)

        # Start DFS with initial OR as 0
        dfs(0, 0)
        return self.count

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.countMaxOrSubsets([3, 1]))      # Output: 2
    print(solution.countMaxOrSubsets([2, 2, 2]))   # Output: 7
    print(solution.countMaxOrSubsets([3, 2, 1, 5]))# Output: 6
