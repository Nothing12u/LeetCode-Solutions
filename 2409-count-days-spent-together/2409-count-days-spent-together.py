class Solution:
    def countDaysTogether(self, aa: str, la: str, ab: str, lb: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def f(s:str):
            m=int(s[:2])
            n=int(s[3:])
            return sum(days[:m-1])+n
        a=f(aa)
        b=f(la)
        c=f(ab)
        d=f(lb)
        start=max(a,c)
        end=min(b,d)
        return max(0,end-start+1)