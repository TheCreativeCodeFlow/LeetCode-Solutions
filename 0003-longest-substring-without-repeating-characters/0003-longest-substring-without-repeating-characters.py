class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp=[0]*128
        ml=0
        left=0
        for right, ch in enumerate(s):
            ascival=ord(ch)
            if lp[ascival]>left:
                left=lp[ascival]
            lp[ascival]=right+1
            cur=right-left+1
            if cur>ml:
                ml=cur
        return ml