class Solution:
    def checkString(self, s: str) -> bool:
        a=-1
        b=-1
        for i in range(len(s)):
            if s[i]=='b':
                b=i
                break
        for i in range(len(s)):
            if s[i]=='a':
                a=i
        return a<b or b==-1