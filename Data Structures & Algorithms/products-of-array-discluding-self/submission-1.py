class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        for i in range(1,len(nums)):
            left[i]=(nums[i-1]*left[i-1])

        right = [1] * len(nums)
        for j in range(len(nums)-2,-1,-1):
            right[j] =(nums[j+1]*right[j+1])

        return [left[n]*right[n] for n in range(len(nums))]
        