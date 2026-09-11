class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        return  sum(1  for a,b,c in {*permutations(digits,3)} if a and c&1==0)
        