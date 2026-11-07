class Solution:
    def countValidSubstrings(self, s: str) -> int:
        n=len(s)
        total=n*(n+1)//2
        last=-1
        invalid=0
        for i in range(2,n):
            if s[i-2]=='a' and s[i-1]=='b' and s[i]=='c':
                last=i
            if last!=-1:
                invalid+=(last-1)
        return total-invalid