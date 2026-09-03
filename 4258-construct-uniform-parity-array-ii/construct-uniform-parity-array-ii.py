class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        if nums1[0]%2==1:
            return True
        for ele in nums1:
            if ele%2==1:
                return False
        return True