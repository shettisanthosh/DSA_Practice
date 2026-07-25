class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h=[-1]*(256)
        l=0;r=0;maxx=0;n=len(s)
        while r<n:
            if h[ord(s[r])]!=-1:
                if h[ord(s[r])]>=l:
                    l=h[ord(s[r])]+1
            h[ord(s[r])]=r
            length=r-l+1
            maxx=max(maxx,length)
            r+=1
        return maxx