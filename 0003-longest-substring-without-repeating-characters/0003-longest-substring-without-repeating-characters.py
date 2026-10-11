class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        se=set()
        ml=0
        for i in range(len(s)):
            if s[i] not in se:
                se.add(s[i])
            else:
                while s[i] in se:
                    se.remove(s[l])
                    l+=1
            se.add(s[i])
            ml=max(ml,i-l+1)
        return ml