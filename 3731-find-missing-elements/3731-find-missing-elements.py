class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a,b=max(nums),min(nums)
        c=[]
        for i in range(b,a+1):
            c.append(i)
        d=[]
        for i in range(len(c)):
            if c[i] not in nums:
                d.append(c[i])
        return d