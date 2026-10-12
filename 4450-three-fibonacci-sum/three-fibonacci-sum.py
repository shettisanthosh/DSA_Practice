class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        def is_fibonacci(n):
            a,b=0,1
            while a<n:
                a,b=b,a+b
            return a==n
        if n%2==1:
            return False
        else:
            return is_fibonacci(n//2)