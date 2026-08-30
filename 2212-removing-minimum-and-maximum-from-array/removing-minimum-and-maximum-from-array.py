class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_idx=nums.index(min(nums))
        max_idx=nums.index(max(nums))
        left=min(min_idx,max_idx)
        right=max(min_idx,max_idx)
        from_front=right+1
        from_back=len(nums)-left
        from_both=(left+1)+(len(nums)-right)
        return min(from_front,from_back,from_both)