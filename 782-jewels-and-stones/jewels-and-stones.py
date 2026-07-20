class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew=set(jewels)
        c=0
        for s in stones:
            if s in jew:
                c+=1
        return c