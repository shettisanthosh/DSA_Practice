class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened=0
        ans=""
        for ch in s:
            if ch=='(':
                if opened>0:
                    ans+=ch
                opened+=1
            elif ch==')':
                opened-=1
                if opened>0:
                    ans+=ch
        return ans