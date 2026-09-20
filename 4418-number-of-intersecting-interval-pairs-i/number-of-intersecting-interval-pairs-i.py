class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        count=0
        n=len(intervals)
        intervals.sort()
        for i in range(n):
            for j in range(i+1,n):
                if intervals[i][1]>=intervals[j][0]:
                    count+=1
                else:
                    break
        return count