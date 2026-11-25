class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        map = {}
        for i in nums:
            if i in map:
                return True;
            map[i]=i
        return False

a = Solution()
print(a.hasDuplicate([1,2,3,4]))
print(a.hasDuplicate([1,2,3,3]))
print(a.hasDuplicate([1,2,3,4,5,6,7,1]))
        