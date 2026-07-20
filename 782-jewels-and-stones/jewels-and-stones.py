from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        di=dict(Counter(stones))
        count=0
        for c in jewels:
            if c in di:
                count+=di[c]
        return count