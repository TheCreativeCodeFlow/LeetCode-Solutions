class Solution:
    def countGoodStrings(self, n: int) -> int:
        MOD=10**9+7
        m=n
        def fib(n):
            if n==0:
                return (0,1)
            a,b=fib(n//2)
            c=(a*((2*b-a)%MOD))%MOD
            d=(a*a+b*b)%MOD
            if n%2==0:
                return (c,d)
            else:
                return (d,(c+d)%MOD)
        return (2*fib(m)[0])%MOD