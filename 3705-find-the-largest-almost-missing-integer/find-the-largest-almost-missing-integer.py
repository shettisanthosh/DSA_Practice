from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==n:
            return max(nums)
        count=Counter(nums)
        if k==1:
            arr=[x for x in nums if count[x]==1]
        else:
            arr=[x for x in (nums[0],nums[-1]) if count[x]==1] 
        return max(arr) if arr else -1