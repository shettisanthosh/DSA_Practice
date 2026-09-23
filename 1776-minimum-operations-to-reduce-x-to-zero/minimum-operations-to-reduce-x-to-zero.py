class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        aim=sum(nums)-x
        if aim<0:
            return -1
        left=0;curr=0;longest=0
        for right in range(len(nums)):
            curr+=nums[right]
            while curr>aim:
                curr-=nums[left]
                left+=1
            if curr==aim:
                longest=max(longest,right-left+1)
        if aim>0 and longest==0:
            return -1
        return len(nums)-longest