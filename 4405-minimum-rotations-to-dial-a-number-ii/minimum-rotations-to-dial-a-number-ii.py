class Solution:
    def minRotations(self, n: int, s: str) -> int:
        a=list(map(int,s))
        def cost(x,y):
            diff=abs(x-y)
            return min(diff,10-diff)
        base=cost(0,a[0])
        for i in range(1,n):
            base+=cost(a[i-1],a[i])
        ans=base
        ans=min(ans,base-cost(0,a[0])+cost(0,a[n-1]))
        for k in range(1,n):
            new=base-cost(a[k-1],a[k])+cost(a[k-1],a[n-1])
            ans=min(ans,new)
        return ans