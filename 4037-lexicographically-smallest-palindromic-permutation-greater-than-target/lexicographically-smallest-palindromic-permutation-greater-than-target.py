class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n=len(s)
        count=[0]*26
        for ch in s:
            count[ord(ch)-ord('a')]+=1
        oddCount=0
        midChar='$'
        for c in range(26):
            if count[c]%2==1:
                oddCount+=1
                midChar=chr(c+ord('a'))
        if oddCount>1:
            return ""
        for c in range(26):
            count[c]//=2
        halfLen=n//2
        result=""
        def solve(curr,i,greater):
            if len(curr)==halfLen:
                left="".join(curr)
                candidate=left
                if midChar!='$':
                    candidate+=midChar
                candidate+=left[::-1]
                if candidate>target:
                    return candidate
                return ""
            for c in range(26):
                if count[c]==0:
                    continue
                ch=chr(c+ord('a'))
                if not greater and ch<target[i]:
                    continue
                curr.append(ch)
                count[c]-=1
                isGreater=greater or (ch>target[i])
                result=solve(curr,i+1,isGreater)
                curr.pop()
                count[c]+=1
                if result!="":
                    return result
            return ""
        return solve([],0,False)

