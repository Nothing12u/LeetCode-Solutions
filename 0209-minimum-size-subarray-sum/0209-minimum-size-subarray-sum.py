class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        c=0
        ml=float("inf")
        for i in range(len(nums)):
            c+=nums[i]
            while c>=target:
                ml=min(ml,i-l+1)
                c-=nums[l]
                l+=1
        if ml==float("inf"):
            return 0
        else:
            return ml
