class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        count = 0
        for i in range(len(prices) -1):
            count = count + max(prices[i+1] - prices[i], 0)

        return count 
