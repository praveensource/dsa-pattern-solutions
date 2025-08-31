Count the number of subarrays with XOR = k.
"""
Link ---->>> https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1
Approaches:
1. Brute Force (O(n^2))
2. Optimized using Prefix XOR + Hashmap (O(n))
"""

from collections import defaultdict

class Solution:
    # Brute Force: O(n^2)
    def subarrayXorBrute(self, arr, k):
        n = len(arr)
        count = 0
        for i in range(n):
            total = 0
            for j in range(i, n):
                total ^= arr[j]   # XOR from i → j
                if total == k:
                    count += 1
        return count

    # Optimized: O(n)
    def subarrayXorOptimized(self, arr, k):
        total = 0
        count = 0
        mpp = defaultdict(int)
        mpp[0] = 1  # handle case when subarray itself = k

        for num in arr:
            total ^= num
            remove = total ^ k
            count += mpp[remove]
            mpp[total] += 1
        return count


if __name__ == "__main__":
    arr = [4, 2, 2, 6, 4]
    k = 6
    sol = Solution()

    print("Brute Force:", sol.subarrayXorBrute(arr, k))       # 4
    print("Optimized:", sol.subarrayXorOptimized(arr, k))     # 4
