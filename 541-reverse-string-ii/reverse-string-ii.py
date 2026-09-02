class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        st=list(s)
        for i in range(0,len(s),2*k):
            st[i:i+k]=reversed(st[i:i+k])
        return "".join(st)