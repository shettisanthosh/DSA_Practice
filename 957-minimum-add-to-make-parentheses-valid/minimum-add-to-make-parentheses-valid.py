class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened=0;add=0
        for ch in s:
            if ch=='(':
                opened+=1
            else:
                if opened>0:
                    opened-=1
                else:
                    add+=1
        return add+opened