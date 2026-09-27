from collections import Counter
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        count=Counter(nums)
        ans=[]
        for _ in range(max(count.values()) if count else 0):
            for val in sorted(count.keys()):
                if count[val]>0:
                    ans.append(val)
                    count[val]-=1
        return ans
