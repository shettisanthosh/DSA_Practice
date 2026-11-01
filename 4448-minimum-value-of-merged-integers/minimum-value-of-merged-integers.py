class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        arr=[]
        n=len(nums)
        i=0;j=1
        while i<n and j<n:
            s=str(nums[i])+str(nums[j])
            arr.append(int(s))
            i+=2
            j+=2
        return min(arr)
        
