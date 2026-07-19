from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq=Counter(s)
        stack=[]
        seen=set()
        for c in s:
            freq[c]-=1
            if c in seen:
                continue
            while stack and stack[-1]>c and freq[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return "".join(stack)
