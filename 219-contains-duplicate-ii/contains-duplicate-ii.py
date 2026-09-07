class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp={}
        for j in range(len(nums)):
            val=nums[j]
            if val in mp and j-mp[val]<=k:
                return True
            mp[val]=j
        return False