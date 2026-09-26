class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        i=0;n=len(s);res=""
        d=dict(knowledge)
        while(i<n):
            if s[i]!='(':
                res+=s[i]
            else:
                i+=1
                temp=""
                while i<n and s[i]!=')':
                    temp+=s[i]
                    i+=1
                res+=d.get(temp,"?")
            i+=1
        return res