class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        c=0
        d=0
        for i in range((n*2)+1):
            if i%2!=0:
                c+=i
            else:
                d+=i
        return d-c
        