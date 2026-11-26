class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        ans = set()
        i=0
        while i<len(nums):
            if nums[i] > 0:
                break
            j,k=i+1,len(nums)-1
            while j<k:
                if nums[j] + nums[k] == -nums[i]:
                    ans.add(tuple([nums[i],nums[j],nums[k]]))
                    j+=1
                    k-=1
                elif nums[j] + nums[k] > -nums[i]:
                    k-=1
                else:
                    j+=1
            i+=1
        return [list(i) for i in ans]