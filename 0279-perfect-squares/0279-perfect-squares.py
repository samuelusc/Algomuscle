class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(1, int(n**0.5) + 1):
            for j in range(i*i, n+1):
                dp[j]= min(dp[j], dp[j-i*i]+1)

        return dp[-1] 