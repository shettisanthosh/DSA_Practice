class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        summ = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                summ += nums[i]
            else:
                break
        num_set = set(nums)
        while summ in num_set:
            summ += 1
        return summ
