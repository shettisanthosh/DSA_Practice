class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch=='(':
                st.append(')')
            elif ch=='{':
                st.append('}')
            elif ch=='[':
                st.append(']')
            else:
                if not st or st.pop()!=ch:
                    return False
        return not st
            