class Solution:
    def minimumSum(self, num: int) -> int:
        arr=[]
        while num>0:
            arr.append(num%10)
            num=num//10
        arr.sort()
        return (arr[0]*10+arr[2])+(arr[1]*10+arr[3])
