class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ns=set(nums)
        ans=k
        while ans in ns:
            ans+=k
        return ans