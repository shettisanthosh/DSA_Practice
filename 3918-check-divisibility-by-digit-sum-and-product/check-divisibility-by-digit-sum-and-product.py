class Solution:
    def checkDivisibility(self, n: int) -> bool:
        dsum=0;dprod=1
        temp=n
        while temp>0:
            dsum+=(temp%10)
            dprod*=(temp%10)
            temp//=10 # don't forget about python divsion operator sybau
        return True if n%(dsum+dprod)==0 else False