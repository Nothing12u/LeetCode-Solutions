class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x > 0:
            while x > 0:
                p = x % 10
                ans = ans * 10 + p
                x = x // 10
        else:
            x = -x
            while x > 0:
                p = x % 10
                ans = ans * 10 + p
                x = x // 10
            ans = -ans

        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans