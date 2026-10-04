class Solution:
    def minRotations(self, s: str) -> int:
        tr=0
        curr=0
        for ch in s:
            t=int(ch)
            d=abs(curr-t)
            tr+=min(d, 10-d)
            curr=t
        return tr