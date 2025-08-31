# Problem:
# Given a binary array nums, delete exactly one element.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
#
# Example:
# nums = [1,1,0,1] -> Output: 3
# Explanation: Delete nums[2] = 0, subarray [1,1,1] has length 3.

# ---------------------------------------------------------
# Brute Force Solution (O(n^2) to O(n^3) depending on implementation)
# ---------------------------------------------------------

def longestSubarray_bruteforce(nums):
    """
    Brute force approach:
    - For each index, simulate deleting that element.
    - Traverse the array to find the longest consecutive run of 1s.
    - Track the maximum length across all deletions.
    
    Time Complexity: O(n^2)  (outer loop for deletion * inner loop for traversal)
    Space Complexity: O(1)
    """
    n = len(nums)
    max_len = 0
    
    for i in range(n):
        count = 0
        curr_max = 0
        for j in range(n):
            if j == i:
                continue  # skip the deleted element
            if nums[j] == 1:
                count += 1
                curr_max = max(curr_max, count)
            else:
                count = 0
        max_len = max(max_len, curr_max)
    
    return max_len


# ---------------------------------------------------------
# Optimized Sliding Window Solution (O(n))
# ---------------------------------------------------------

def longestSubarray(nums):
    """
    Optimized sliding window approach:
    - Use two pointers (left, right) to maintain a window containing at most ONE zero.
    - If the window has more than one zero, move the left pointer until valid.
    - The maximum length is (right - left), since one deletion is mandatory.
    
    Time Complexity: O(n)  (each element visited at most twice)
    Space Complexity: O(1)
    """
    left = 0
    zero_count = 0
    max_len = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        
        # shrink window if more than one zero
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        # (right - left) instead of (right - left + 1) 
        # because we must delete one element
        max_len = max(max_len, right - left)
    
    return max_len


# ---------------------------------------------------------
# Example Runs
# ---------------------------------------------------------
if __name__ == "__main__":
    nums1 = [1,1,0,1]
    nums2 = [0,1,1,1,0,1,1,0,1]
    nums3 = [1,1,1]
    
    print("Brute Force:")
    print(longestSubarray_bruteforce(nums1))  # 3
    print(longestSubarray_bruteforce(nums2))  # 5
    print(longestSubarray_bruteforce(nums3))  # 2

    print("\nOptimized:")
    print(longestSubarray(nums1))  # 3
    print(longestSubarray(nums2))  # 5
    print(longestSubarray(nums3))  # 2
