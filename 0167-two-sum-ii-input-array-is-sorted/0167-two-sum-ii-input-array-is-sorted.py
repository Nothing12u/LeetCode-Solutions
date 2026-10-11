class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        l=0
        m=len(n)-1
        while m>l:
            mid=n[l]+n[m]
            if mid==t:
                return [l+1,m+1]
            elif mid>t:
                m-=1
            else:
                l+=1
            
        