class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        minn=float('inf')
        for x,y in tasks:
            minn=min(minn,(x+y))
        return minn