class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * 3
        # following the fibonacci sequence pattern
        dp[1],dp[2] = 1,2
        for i in range(3,n+1):
            sum = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = sum

        return dp[2]
