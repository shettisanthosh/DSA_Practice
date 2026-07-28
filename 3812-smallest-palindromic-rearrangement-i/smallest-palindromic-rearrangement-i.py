class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l=len(s)
        count=[0]*26
        slist=[""]*l
        m=0
        n=l-1
        th=0
        for ch in s:
            count[ord(ch)-ord('a')]+=1
        for i in range(26):
            if count[i]==0:
                continue
            if count[i]%2==0:
                while count[i]>0:
                    slist[m]=chr(i+97)
                    m+=1
                    slist[n]=chr(i+97)
                    n-=1
                    count[i]-=2
            else:
                th=i
                while count[i]>1:
                    slist[m]=chr(i+97)
                    m+=1
                    slist[n]=chr(i+97)
                    n-=1
                    count[i]-=2
        if l%2!=0:
            slist[m]=chr(th+97)
        return "".join(slist)

        