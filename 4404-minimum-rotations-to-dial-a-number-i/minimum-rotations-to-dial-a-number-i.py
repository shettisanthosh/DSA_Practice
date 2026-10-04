class Solution:
    def minRotations(self, s: str) -> int:
        ans=0;prev=0
        for ch in s:
            curr=int(ch)
            diff=abs(curr-prev)
            ans+=min(diff,10-diff)
            prev=curr
        return ans
            