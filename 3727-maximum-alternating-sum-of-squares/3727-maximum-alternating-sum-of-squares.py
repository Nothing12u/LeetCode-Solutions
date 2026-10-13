class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs)
        ec=0
        oc=0
        h=len(nums)//2
        for i in range(len(nums)):
            if i<h:
                oc+=nums[i]**2
            else:
                ec+=nums[i]**2
        return ec-oc