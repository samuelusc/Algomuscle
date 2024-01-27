class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(1,len(prices)):
            res = res + max(prices[i] - prices[i-1], 0)

        return res


        #p(1）买 p(3) 卖 相当于 p(3)-p(2) + p(2)-p(1) 
        # once the array is in monotonically decreasing order, 0 is output
        # we can pick the max(0, with p[i]-p[i-1])