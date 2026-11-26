class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        low = prices[0]
        i = 0
        res=0        
        for i in range(1,len(prices)):
            if prices[i]>low:
                res = max(prices[i]-low,res)
            elif prices[i]<low:
                low =prices[i]
        return res
                

        