class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        MOD=10**9+7
        base=max(nums)+1
        def check(k):
            p=pow(base,k-1,MOD)
            h=0
            mp={}
            for j in range(len(nums)):
                h=(h*base+nums[j])%MOD
                if j>=k-1:
                    mp[h]=mp.get(h,0)+1
                    i=j-k+1
                    h=(h-p*nums[i])%MOD
            return 1 in mp.values()
        l,r=1,len(nums)
        ans=len(nums)
        while l<=r:
            mid=(l+r)//2
            if check(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans