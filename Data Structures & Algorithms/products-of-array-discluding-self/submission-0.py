class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        p = 1
        for i in range(1,len(nums)):
            left[i]=(nums[i-1]*p)
            p=left[i]
        
        right = [1] * len(nums)
        q=1
        for j in range(len(nums)-2,-1,-1):
            right[j] =(nums[j+1]*q)
            q = right[j]

        ans = []
        for n in range(len(nums)):
            ans.append(left[n]*right[n])
        return ans
        