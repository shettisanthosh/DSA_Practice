class Solution:
    def minRotations(self, s: str) -> int:
        arr=[0,9,8,7,6,5,4,3,2,1]
        ans=0
        for i in range(len(s)):
            if i==0:
                num1=int(s[i])
            else:
                num1=abs(int(s[i])-int(s[i-1]))
            p1=0
            while arr[p1]!=num1:
                p1+=1
            ans+=min(num1,p1)
        return ans
            