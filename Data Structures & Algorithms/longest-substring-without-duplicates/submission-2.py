class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        res = 0
        start = 0
        for i,a in enumerate(s):
            if a in d and d[a]>=start:
                res = max(i-start,res)
                start = d[a]+1
            d[a]=i
        return max(res,len(s)-start)
            



        