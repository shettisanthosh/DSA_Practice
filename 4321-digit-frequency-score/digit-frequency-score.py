class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=0
        while n>0:
            d=n%10
            s+=d
            n//=10
        return s