class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1

        while i<j:
            while i<j and not s[i].isalnum():
                i +=1
            if i>j:
                print(i,s[i],j,s[j],1)
                return False
            while i<j and not s[j].isalnum():
                j-= 1
            if i>j:
                print(i,s[i],j,s[j],2)
                return False
            if s[i].lower()!=s[j].lower():
                print(i,s[i],j,s[j],3)
                return False
            else:
                i +=1
                j -= 1
        return True
        