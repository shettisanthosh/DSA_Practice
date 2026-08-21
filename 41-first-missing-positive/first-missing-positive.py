class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l=len(nums)
        for i in range(l):
            if 1<=nums[i]<=l:
                continue
            else:
                nums[i]=l+1
        for i in range(l):
            num=abs(nums[i])
            if num==l+1:
                continue
            else:
                if nums[num-1]>0:
                    nums[num-1]=-nums[num-1]
        for i in range(l):
            if nums[i]>0:
                return i+1
        return l+1