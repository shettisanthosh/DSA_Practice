class Solution:
    def canAliceWin(self, n: int) -> bool:
        k=(21-(441-8*n)**0.5)//2
        return k%2==1