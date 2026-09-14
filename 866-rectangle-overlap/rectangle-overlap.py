class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec2[2]<=rec1[0]:
            return False
        if rec1[2]<=rec2[0]:
            return False
        if rec2[1]>=rec1[3]:
            return False
        if rec1[1]>=rec2[3]:
            return False
        return True