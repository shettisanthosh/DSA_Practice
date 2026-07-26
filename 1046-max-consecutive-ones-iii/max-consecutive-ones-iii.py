class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lnth=0;maxl=0;l=0;r=0;z=0
        while r<len(nums):
            if nums[r]==0:
                z+=1
            while z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            lnth=r-l+1
            maxl=max(maxl,lnth)
            r+=1
        return maxl