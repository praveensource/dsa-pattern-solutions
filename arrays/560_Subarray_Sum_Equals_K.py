560_Subarray_Sum_Equals_K
Link -- > https://leetcode.com/problems/subarray-sum-equals-k/

## Approach (Prefix Sum + Hashmap)
1. Use a **running prefix sum** (`total`) while traversing the array.  
2. For each index, check if `(total - k)` exists in the hashmap.  
   - If yes, then a subarray ending at the current index sums to `k`.  
3. Store/update prefix sums in the hashmap to keep track of their occurrences.  
4. Accumulate the total count.  

This avoids the brute force O(n²) checking of all subarrays.

---

## Complexity
- **Time Complexity:** `O(n)` → single pass through array.  
- **Space Complexity:** `O(n)` → hashmap stores prefix sums.  

---

## Code

```python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mpp = defaultdict(int)  # stores prefix sum frequencies
        mpp[0] = 1              # base case: sum=0 before starting
        total = 0               # running prefix sum
        count = 0               # total subarrays count

        for num in nums:
            total += num
            remove = total - k
            count += mpp[remove]   # check if subarray sum == k
            mpp[total] += 1        # store/update prefix sum frequency
        
        return count
