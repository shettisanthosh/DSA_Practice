class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=set()
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                curr=nums[i]+nums[l]+nums[r]
                if curr==0:
                    result.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif curr<0:
                    l+=1
                else:
                    r-=1
        return [list(triplet) for triplet in result]