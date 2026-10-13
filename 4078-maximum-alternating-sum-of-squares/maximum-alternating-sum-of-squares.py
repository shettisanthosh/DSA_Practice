class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        l=len(nums)
        i=0;j=l-1
        nums.sort()
        s=0
        n=l//2
        if l%2==0:
            while n>0:
                if abs(nums[i])>=abs(nums[j]):
                    s+=nums[i]**2
                    i+=1
                else:
                    s+=nums[j]**2
                    j-=1
                n-=1
        else:
            while n+1>0:
                if abs(nums[i])>=abs(nums[j]):
                    s+=nums[i]**2
                    i+=1
                else:
                    s+=nums[j]**2
                    j-=1
                n-=1
        for m in range(i,j+1):
            s-=nums[m]**2
        return s