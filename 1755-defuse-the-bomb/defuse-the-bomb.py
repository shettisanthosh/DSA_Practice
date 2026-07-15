# 1st approach came to mind.
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        lnth=len(code)
        count=[0]*lnth
        if k==0:
            return count
        elif k>0:
            for i in range(lnth):
                l=(i+1)%lnth
                r=(i+k)%lnth
                count[i]=sum(code[l:r+1]) if l<=r else sum(code[l:])+sum(code[:r+1])
        else:
            for i in range(lnth):
                l=(i-abs(k))%lnth
                r=(i-1)%lnth
                count[i]=sum(code[l:r+1]) if l<=r else sum(code[l:])+sum(code[:r+1])
        return count

#After identifying pattern.
from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        if k == 0:
            return result
        if k > 0:
            l = 1
            r = k
        else:
            l = n - abs(k)
            r = n - 1
        window_sum = 0
        for i in range(l, r + 1):
            window_sum += code[i]
        for i in range(n):
            result[i] = window_sum
            window_sum -= code[l % n]
            l += 1
            r += 1
            window_sum += code[r % n]
        return result
