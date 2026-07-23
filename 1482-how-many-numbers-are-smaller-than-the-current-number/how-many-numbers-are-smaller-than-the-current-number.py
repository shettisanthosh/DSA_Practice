class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2=[0]*101
        res=[0]*len(nums)
        for i in nums:
            nums2[i]+=1
        for i in range(1,101):
            nums2[i]+=nums2[i-1]
        for i in range(len(nums)):
            j=nums[i]
            if j==0:
                res[i]=0
            else:
                res[i]=nums2[j-1]
        return res
        
        
