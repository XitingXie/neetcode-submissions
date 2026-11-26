class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i,j = 0,len(heights)-1
        while i<j:
            if i>0 and heights[i]<heights[i-1]:
                i+=1
                continue
            if j<len(heights)-1 and heights[j]<heights[j+1]:
                j -= 1
                continue
            area = min(heights[i],heights[j]) * (j-i)
            res = max(res,area)
            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1
        return res

        