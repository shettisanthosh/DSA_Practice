import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        mx=-1
        preGcd=[]
        for i in range(n):
            mx=max(mx,nums[i])
            preGcd.append(math.gcd(nums[i],mx))
        preGcd.sort()
        res=0
        for i in range(n//2):
            res+=math.gcd(preGcd[i],preGcd[n-i-1])
        return res
        