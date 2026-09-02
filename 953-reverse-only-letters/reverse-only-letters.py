class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        st=list(s)
        i=0;j=len(st)-1
        while i<j:
            if st[i].isalpha() and st[j].isalpha():
                st[i],st[j]=st[j],st[i]
                i+=1
                j-=1
            else:
                if not st[i].isalpha():
                    i+=1
                else:
                    j-=1
        return "".join(st)