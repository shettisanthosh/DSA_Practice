import numpy as np
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums)
        nums_arr=np.array(nums)
        mid=n//2
        nums_arr.partition(mid)
        mid_v=nums_arr[mid]
        moves=0
        for i in range(mid):
            moves+=abs(nums_arr[i]-mid_v)
            moves+=abs(nums_arr[n-i-1]-mid_v)
        return int(moves)