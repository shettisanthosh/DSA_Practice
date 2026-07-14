class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i]+=(nums[n+i]%1024)*1024
        for i in range(n-1,-1,-1):
            nums[2*i+1]=nums[i]//1024
            nums[2*i]=nums[i]%1024
        return nums