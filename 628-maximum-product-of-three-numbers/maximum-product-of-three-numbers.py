class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        fL=sL=tL=-1001
        fS=sS=1001
        for num in nums:
            temp1,temp2,temp3=fL,sL,fS
            fL=max(fL,num)
            sL=max(sL,min(temp1,num))
            tL=max(tL,min(temp2,num))
            fS=min(fS,num)
            sS=min(sS,max(temp3,num))

        return max(fL*sL*tL, fS*sS*fL)