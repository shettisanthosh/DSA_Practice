class Solution:
    def maxDepth(self, s: str) -> int:
        st=[]
        ans=0
        for ch in s:
            if ch=='(':
                st.append(ch)
                ans=max(ans,len(st))
            elif ch==')':
                st.pop()
        return ans