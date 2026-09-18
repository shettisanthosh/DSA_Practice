class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n=len(s)
        st=[-1]*26
        e=[0]*26
        isValid=[True]*26
        res=[]
        for i in range(n):
            idx=ord(s[i])-ord('a')
            if st[idx]==-1:
                st[idx]=i
            e[idx]=i
        for c in range(26):
            if st[c]==-1:
                continue
            i=st[c]
            while i<=e[c]:
                idx=ord(s[i])-ord('a')
                if st[idx]<st[c]:
                    isValid[c]=False
                    break
                e[c]=max(e[c],e[idx])
                i+=1
        lastTaken=float('inf')
        for i in range(n-1,-1,-1):
            c=ord(s[i])-ord('a')
            if not isValid[c]:
                continue
            if i==st[c] and e[c]<lastTaken:
                res.append(s[i:e[c]+1])
                lastTaken=i
        return res