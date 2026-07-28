from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count=Counter(s)
        half=[]
        mid=""
        for ch in sorted(count.keys()):
            if count[ch]%2==1:
                mid=ch
            half.append(ch*(count[ch]//2))
            left="".join(half)
        return left+mid+left[::-1]