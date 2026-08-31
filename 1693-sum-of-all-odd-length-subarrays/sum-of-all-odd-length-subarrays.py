class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+arr[i]
        ans=0
        for i in range(n):
            for j in range(i+1,n+1,2):
                ans+=prefix[j]-prefix[i]
        return ans