class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n=len(arr)
        m=10**9+7
        count=0;even=1;odd=0;summ=0
        for i in range(n):
            summ+=arr[i]
            if summ%2==0:
                count=(count+odd)%m
                even+=1
            else:
                count=(count+even)%m
                odd+=1
        return count