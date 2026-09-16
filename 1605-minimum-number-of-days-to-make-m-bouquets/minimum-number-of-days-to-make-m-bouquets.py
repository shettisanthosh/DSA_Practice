class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        def help(bloomDay,mid,k):
            boqC=0
            cons=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=mid:
                    cons+=1
                else:
                    cons=0
                if cons==k:
                    boqC+=1
                    cons=0
            return boqC
        start=0;end=max(bloomDay);minD=-1
        while start<=end:
            mid = (start+end)//2
            if help(bloomDay,mid,k)>=m:
                minD=mid
                end=mid-1
            else:
                start=mid+1
        return minD