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


                
