class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i,j = 0,len(heights)-1
        while i<j:
            if(i>0) and heights[i] < heights[i-1]:
                i+=1
                continue
            s = min(heights[i],heights[j]) * (j - i)
            res = max(s,res)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return res

        