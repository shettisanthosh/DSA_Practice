class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i=0 #even
        j=1 #odd
        n=len(nums)
        while i<n and j<n:
            if nums[i]%2==1 and nums[j]%2==0:
                nums[i],nums[j]=nums[j],nums[i]
            if nums[i]%2==0:
                i+=2
            if nums[j]%2==1:
                j+=2
        return nums