from math import gcd,lcm
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            p=1
            g=0
            l=1
            for j in range(i,len(nums)):
                x=nums[j]
                p*=x
                g=gcd(g,x)
                l=lcm(l,x)
                if p==g*l:
                    ans=max(ans,j-i+1)
        return ans