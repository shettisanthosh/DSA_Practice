class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        if n==10:
            return True
        temp=n;num=10;i=0
        while temp>=num:
            temp=temp-num
            i=i+1
            num=num-1
        if i%2==0:
            return False
        else:
            return True