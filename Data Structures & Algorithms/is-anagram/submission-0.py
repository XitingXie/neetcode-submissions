from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = defaultdict(int)
        for c in s:
            d_s[c] += 1

        for d in t:
            if d in d_s:
                d_s[d]-=1
                if d_s[d] == 0:
                    del d_s[d]
            else:
                return False
        
        if len(d_s) > 0:
            return False
        return True
        