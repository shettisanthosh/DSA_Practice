class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        maxx=max(nums)
        n=len(nums)
        t=1
        while t<=maxx:
            t=t*2
        s1=[False]*(t)
        s2=[False]*(t)
        for i in range(n):
            for j in range(i,n):
                s1[nums[i]^nums[j]]=True
        for i in range(t):
            if s1[i]==True:
                for num in nums:
                    s2[i^num]=True
        res=0
        for i in range(t):
            if s2[i]:
                res+=1
        return res

