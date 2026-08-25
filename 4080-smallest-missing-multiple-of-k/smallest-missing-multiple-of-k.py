class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        count=[0]*1000000
        for i in range(len(nums)):
            if nums[i]%k==0:
                count[nums[i]]=1
        for i in range(k,1000000,k):
            if count[i]==0:
                return i
        return -1
