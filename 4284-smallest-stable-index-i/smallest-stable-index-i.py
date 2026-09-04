class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mx=0;mn=0
        for i in range(len(nums)):
            mx=max(nums[:i+1])
            mn=min(nums[i:])
            cv=mx-mn
            if cv<=k:
                return i
        return -1