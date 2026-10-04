class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        t=[[-1]*101 for i in range(101)]
        def solve(idx,openn):
            if idx==n:
                return openn==0
            if t[idx][openn]!=-1:
                return t[idx][openn]==1
            isValid=False
            if s[idx]=="*":
                if openn>0:
                    isValid|=solve(idx+1,openn-1)
                isValid|=solve(idx+1,openn+1)
                isValid|=solve(idx+1,openn)
            elif s[idx]=="(":
                isValid|=solve(idx+1,openn+1)
            elif openn>0:
                isValid|=solve(idx+1,openn-1)
            t[idx][openn]=1 if isValid else 0
            return isValid 
        return solve(0,0)

