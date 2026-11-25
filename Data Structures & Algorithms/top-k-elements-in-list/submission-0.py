class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_n = max(nums)
        min_n = min(nums)
        d = [0] * (max_n - min_n+1)

        for n in nums:
            d[n - min_n] += 1
        
        result = []
        for i in range(k):
            k,max_n = 0,d[0]
            for j,c in enumerate(d):
                if c > max_n:
                    max_n = c
                    k = j
            if d[k]>0:
                result.append(k+min_n) 
                d[k]=-1
        
        return result
        