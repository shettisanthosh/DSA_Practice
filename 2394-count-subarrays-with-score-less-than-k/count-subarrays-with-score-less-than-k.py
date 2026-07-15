class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        total=0;result=0;i=0;j=0;n=len(nums)
        while j<n:
            total+=nums[j]
            while i<=j and total*(j-i+1)>=k:
                total-=nums[i]
                i+=1
            result+=(j-i+1)
            j+=1
        return result