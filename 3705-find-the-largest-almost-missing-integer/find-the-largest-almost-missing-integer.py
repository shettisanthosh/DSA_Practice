class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=[0]*51
        for i in range(n-k+1):
            curr=nums[i:i+k]
            uniq=set(curr)
            for ele in uniq:
                count[ele]+=1
        for i in range(50,-1,-1):
            if count[i]==1:
                return i
        return -1