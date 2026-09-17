class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n=len(arr)
        i=0;j=0;currSum=0
        minBest=[float('inf')]*n
        bestMinLen=float('inf')
        res=float('inf')
        while j<n:
            currSum+=arr[j]
            while i<j and currSum>target:
                currSum-=arr[i]
                i+=1
            if currSum==target:
                length=j-i+1
                if i>0 and minBest[i-1]!=float('inf'):
                    res=min(res,length+minBest[i-1])
                bestMinLen=min(bestMinLen,length)
            minBest[j]=bestMinLen
            j+=1
        return -1 if res==float('inf') else res