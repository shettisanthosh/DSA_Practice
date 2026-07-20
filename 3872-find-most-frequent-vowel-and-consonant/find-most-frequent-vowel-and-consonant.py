from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        di=dict(Counter(s))
        vowels="aeiou"
        maxx1=0;maxx2=0
        for key,value in di.items():
            if key in vowels:
                maxx1=max(maxx1,di[key])
            else:
                maxx2=max(maxx2,di[key])
        return maxx1+maxx2


