class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        xor=0
        for num in nums:
            if num%2==0:
                xor|=num
        return xor