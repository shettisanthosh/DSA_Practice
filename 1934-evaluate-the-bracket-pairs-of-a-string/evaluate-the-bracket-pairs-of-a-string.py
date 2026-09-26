class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len(s)
        mp = dict(knowledge)
        result = ""
        i = 0
        while i < n:
            if s[i] == '(':
                j = s.find(")", i + 1)
                temp = s[i + 1 : j]
                result += mp.get(temp,"?")
                i = j
            else:
                result += s[i]
            i += 1      
        return result
