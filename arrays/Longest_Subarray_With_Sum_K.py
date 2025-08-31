class Solution:
    def longestSubarray(self, arr, k):  
        """
        Problem: 
	Link ---->>>>> https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
        Given an array arr and an integer k, 
        find the length of the longest subarray whose sum equals k.
        
        Approach:
        - Use prefix sum + hashmap to store first occurrence of prefix sums.
        - If total - k exists in map, we found a subarray with sum = k.
        """

        preSum_map = {}   # Stores {prefix_sum: first_index}
        maxLen = 0        # Stores max length of subarray
        total = 0         # Running prefix sum

        for i in range(len(arr)):
            total += arr[i]   # Update prefix sum

            # Case 1: Subarray from index 0 → i has sum = k
            if total == k:
                maxLen = max(maxLen, i + 1)

            # Case 2: Subarray between indices (preSum_map[total-k]+1 ... i)
            remaining = total - k
            if remaining in preSum_map:
                length = i - preSum_map[remaining]
                maxLen = max(maxLen, length)

            # Store prefix sum in map if not already present
            if total not in preSum_map:
                preSum_map[total] = i

        return maxLen


        """
        ✅ Time Complexity (TC): O(n)
           - We iterate through the array once.
           - Each lookup/update in hashmap is O(1) average.

        ✅ Space Complexity (SC): O(n)
           - In worst case, we store all prefix sums in hashmap.
        """
