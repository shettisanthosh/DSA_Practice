class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        p1=0;p2=1;summ=nums[0]
        while p2!=len(nums):
            if nums[p2]-nums[p1]==1:
                p1+=1
                p2+=1
                summ+=nums[p1]
            else:
                break
        for i in range(50):
            if summ in nums:
                summ+=1
            else:
                break
        return summ