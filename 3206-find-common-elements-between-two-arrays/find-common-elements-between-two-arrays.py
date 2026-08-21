class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[0]*2
        for ele in nums1:
            if ele in nums2:
                ans[0]+=1
        for ele in nums2:
            if ele in nums1:
                ans[1]+=1
        return ans