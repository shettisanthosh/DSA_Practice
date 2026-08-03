class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r=0;count=0
        for i in range(len(s)):
            if s[i]=='R':
                r+=1
            else:
                r-=1
            if r==0:
                count+=1
        return count
            