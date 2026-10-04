class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        t=nums
        n=float('-inf')
        p=n
        m=n
        dp=n
        dm=n
        ans=n
        for x in nums:
            op=p
            om=m
            odp=dp
            odm=dm
            p=x
            m=n
            if om!=n:
                p=max(p,om+x)
            if op!=n:
                m=op-x
            dp=op
            dm=om
            if odm!=n:
                dp=max(dp,odm+x)
            if odp!=n:
                dm=max(dm,odp-x)
            ans=max(ans,p,m,dp,dm)
        return ans