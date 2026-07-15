class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        #sliding window template
        total=0;result=0;i=0;j=0;n=len(nums) #variables declared in 1 line on purpose
        while j<n:
            total+=nums[j]
            while i<=j and total*(j-i+1)>=k: #shrink the window until it gets valid
                total-=nums[i] 
                i+=1 
            result+=(j-i+1) #hence it is valid, discover how many valid subarrays exists within that subarray
            j+=1
        return result
