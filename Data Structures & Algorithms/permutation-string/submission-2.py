class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = [0]*26
        for s in s1:
            s1_hash[ord(s) - ord('a')]+=1

        
        i = 0
        while i<=len(s2)-len(s1):
            j=i
            s2_hash = [0]*26
            while j-i < len(s1):
                if s1_hash[ord(s2[j]) - ord('a')]>0:
                    s2_hash[ord(s2[j]) - ord('a')] +=1
                else:
                    break
                j+=1

            if s2_hash == s1_hash:
                return True
            i += 1
        return False            



        