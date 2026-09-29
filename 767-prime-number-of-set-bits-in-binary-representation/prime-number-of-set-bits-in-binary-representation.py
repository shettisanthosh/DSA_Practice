class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:
        return sum((1<<x.bit_count())&((1<<2)|(1<<3)|(1<<5)|(1<<7)|(1<<11)|(1<<13)|(1<<17)|(1<<19))>0 for x in range(l,r+1))