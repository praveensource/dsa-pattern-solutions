class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1

        # find break point
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        if index == -1:
            return nums.reverse()
        # i have to find smaller ie lil greater than present number from last
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break
        
        # i have to make index + 1 all elements to be in sorted
        nums[index + 1:] = reversed(nums[index + 1 : ])

        
