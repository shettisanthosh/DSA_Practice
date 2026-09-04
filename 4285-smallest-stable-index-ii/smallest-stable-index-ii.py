from itertools import accumulate
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        suff_min = list(accumulate(reversed(nums), min))[::-1]
        curr_max = float('-inf')
        for i, num in enumerate(nums):
            curr_max = max(curr_max, num)
            if curr_max - suff_min[i] <= k:
                return i
        return -1
