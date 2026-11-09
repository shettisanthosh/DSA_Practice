class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        return sum(a for a,c in collections.Counter(nums).items() if c==1)