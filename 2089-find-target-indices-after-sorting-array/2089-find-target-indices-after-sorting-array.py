class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        s=[]
        for i in range(len(nums)):
            if nums[i]==target:
                s.append(i)
        return s
