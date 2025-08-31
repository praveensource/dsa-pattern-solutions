class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using map to store value:indeex
        mpp = {}
        for i,num in enumerate(nums):
            mpp[num] = i
        
        # checking
        for i in range(len(nums)):
            y = target - nums[i]
            if y in mpp and mpp[y] != i:
                return [i,mpp[y]]
        return [-1,-1]
        
        
