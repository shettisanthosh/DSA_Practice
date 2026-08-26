class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i=0;j=0;ones=0;n=len(s)
        res=""
        while j<n:
            if s[j]=='1':
                ones+=1
            while ones>k or (i<=j and s[i]=='0'):
                if s[i]=='1':
                    ones-=1
                i+=1
            if ones==k:
                temp=s[i:j+1]
                if res=="" or (j-i+1)<len(res) or (len(res)==len(temp) and temp<res):
                    res=temp
            j+=1
        return res