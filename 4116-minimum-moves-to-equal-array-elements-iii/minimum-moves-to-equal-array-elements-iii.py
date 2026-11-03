class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(abs(max(nums)-num) for num in nums)