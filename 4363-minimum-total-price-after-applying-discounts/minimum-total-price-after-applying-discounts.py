class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        l=len(discounts);m=len(prices)
        k = min(l,m)
        ans=0.0
        for i in range(k):
            ans+=prices[i]*(100-discounts[i])/100
        for i in range(k,m):
            ans+=prices[i]
        return ans
