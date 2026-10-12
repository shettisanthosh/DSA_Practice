class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod=10**9+7
        count=[0]*32
        for num in nums:
            for bit in range(32):
                if num&(1<<bit):
                    count[bit]+=1
        res=0
        while k>0:
            curr=0
            for bit in range(32):
                if count[bit]>0:
                    count[bit]-=1
                    curr=(curr|(1<<bit))
            res=(res+curr**2)%mod
            k-=1
        return res