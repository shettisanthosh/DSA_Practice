from bisect import bisect_right
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n=len(intervals)
        for i in range(n):
            intervals[i].append(i)
        intervals.sort()
        starts=[x[0] for x in intervals]
        next=[bisect_right(starts,intervals[i][1]) for i in range(n)]
        k=4
        dp=[[None]*(k+1) for _ in range(n+1)]
        def solve(i,k):
            if k==0 or i>=n:
                return (0,[])
            if dp[i][k] is not None:
                return dp[i][k]
            skip=solve(i+1,k)
            score,ids=solve(next[i],k-1)
            take=(score+intervals[i][2],ids+[intervals[i][3]])
            take=(take[0],sorted(take[1]))
            if skip[0]>take[0]:
                ans=skip
            elif skip[0]<take[0]:
                ans=take
            else:
                ans=min(skip,take,key=lambda x:x[1])
            dp[i][k]=ans
            return ans
        return solve(0,k)[1]