class Solution:
    def reverseWords(self, s: str) -> str:
        st=""
        l=s.split()
        for i in range(len(l)):
            if i!=len(l)-1:
                st+=l[i][::-1]
                st+=" "
            else:
                st+=l[i][::-1]
        return st
        
            