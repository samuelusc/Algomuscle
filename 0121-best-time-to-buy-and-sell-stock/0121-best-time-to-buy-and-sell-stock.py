class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # define two variables to count the minimum and maximum
        mini = float('inf')
        maxi = 0
        
        for price in prices:
            maxi = max(maxi, price - mini)
            mini = min(mini, price)

        return maxi