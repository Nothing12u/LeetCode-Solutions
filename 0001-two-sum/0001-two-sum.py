class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s={}
        for i in range(len(nums)):
            x=target-nums[i]
            if x in s:
                return [s[x],i]
            s[nums[i]]=i
        