class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq=[0]*10
        for d in digits:
            freq[d]+=1
        ans=0
        for first in range(1,10):
            if freq[first]==0:
                continue
            freq[first]-=1
            for second in range(10):
                if freq[second]==0:
                    continue
                freq[second]-=1
                ans += (freq[0] > 0)
                ans += (freq[2] > 0)
                ans += (freq[4] > 0)
                ans += (freq[6] > 0)
                ans += (freq[8] > 0)
                freq[second]+=1
            freq[first]+=1
        return ans