class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiples={num for num in nums if num%k==0}
        current=k
        while True:
            if current not in multiples:
                return current
            current+=k