from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Problem:
        Given an array of intervals where intervals[i] = [starti, endi],
        merge all overlapping intervals and return an array of non-overlapping intervals
        that cover all the intervals in the input.

        Example:
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlap, they are merged into [1,6].

        Constraints:
        - 1 <= intervals.length <= 10^4
        - intervals[i].length == 2
        - 0 <= starti <= endi <= 10^4

        Approach:
        1. Sort intervals by start time.
        2. Initialize result with the first interval.
        3. Traverse remaining intervals:
            - If current interval overlaps with the last interval in result,
              merge them by updating the end.
            - Otherwise, append the current interval as a new non-overlapping interval.

        Time Complexity: O(n log n)  # sorting dominates
        Space Complexity: O(n)       # result array
        """

        # Step 1: Sort intervals based on start time
        intervals.sort()
        
        # Step 2: Initialize result with the first interval
        merged = [intervals[0]]

        # Step 3: Traverse and merge
        for start, end in intervals[1:]:  # skip the first, already added
            # If overlapping, merge with last interval
            if merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                # Otherwise, add as a new interval
                merged.append([start, end])

        return merged
