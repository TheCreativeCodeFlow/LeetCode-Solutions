class Solution:
    def minRotations(self, n: int, s: str) -> int:
        def dist(a,b):
            d=abs(a-b)
            return min(d,10-d)
        v=s
        t=dist(0,int(s[0]))
        for i in range(1,n):
            t+=dist(int(s[i-1]),int(s[i]))
        ans=t
        for k in range(n):
            if k==0:
                cur=t-dist(0,int(s[0]))+dist(0,int(s[n-1]))
            else:
                cur=t-dist(int(s[k-1]),int(s[k]))+dist(int(s[k-1]),int(s[n-1]))
            ans=min(ans,cur)
        return ans