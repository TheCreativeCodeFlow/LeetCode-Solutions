class Solution(object):
    def sortColors(self, nums):
        low=0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]>nums[i]:
                    low=nums[j]
                    nums[j]=nums[i]
                    nums[i]=low
        
        return nums