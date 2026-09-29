class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        total = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        for num in range(left, right + 1):
            if num.bit_count() in primes: total += 1
        return total
        