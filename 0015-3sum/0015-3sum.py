class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        h=[]
        n=len(nums)
        for i in range(n-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            le,r=i+1,n-1
            while r>le:
                s=nums[i]+nums[le]+nums[r]
                if s<0:
                    le+=1
                elif s>0:
                    r-=1
                else:
                    h.append([nums[i],nums[le],nums[r]])
                    le+=1
                    r-=1
                    while r>le and nums[le]==nums[le-1]:
                        le+=1
                    while r>le and nums[r]==nums[r+1]:
                        r-=1
        return h
