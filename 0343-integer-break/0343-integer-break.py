class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        dp = [0] * (n + 1)
        dp[2] = 1
         
        for i in range(3, n+1):
            for j in range(1, i//2 + 1):
                dp[i] = max(j * (i-j), j * dp[i-j], dp[i])

        return dp[-1]