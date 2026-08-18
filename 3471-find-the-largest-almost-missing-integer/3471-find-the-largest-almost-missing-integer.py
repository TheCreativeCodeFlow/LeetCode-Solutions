class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==1:
            cnt=collections.Counter(nums)
            valid=[x for x, c in cnt.items() if c==1]
            return max(valid) if valid else -1
        if k==n:
            return max(nums)
        ans=-1
        if nums.count(nums[0])==1:
            ans=max(ans, nums[0])
        if nums.count(nums[-1])==1:
            ans=max(ans,nums[-1])
        return ans