class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = float("inf")

        for price in prices:
            maxi = max(maxi, price - mini)
            mini = min(price, mini)

        return maxi