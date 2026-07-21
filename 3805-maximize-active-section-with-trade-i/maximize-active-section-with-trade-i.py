class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        active_count=s.count('1')
        n=len(s)
        inactive=[]
        i=0
        while i<n:
            if s[i]=='0':
                start=i
                while i<n and s[i]=='0':
                    i+=1
                inactive.append(i-start)
            else:
                i+=1
        maxSum=0
        for i in range(1,len(inactive)):
            maxSum=max(maxSum,inactive[i]+inactive[i-1])
        return maxSum+active_count