class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ele=0;xor=True
        for num in nums:
            ele=(ele^num)
            if num!=0:
                xor=False
        if xor:
            return 0
        return len(nums)-1 if ele==0 else len(nums)
        