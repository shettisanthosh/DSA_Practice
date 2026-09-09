class Solution:
    def countCommas(self, n: int) -> int:
        res=0
        lower=1000
        commas=1
        while lower<=n:
            upper=lower*1000-1
            if upper>n:
                upper=n
            count=upper-lower+1
            res+=(commas*count)
            lower*=1000
            commas+=1
        return res

