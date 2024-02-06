class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * 3
        # 不需要考虑 n<2 的情况因为 0， 1 step cost 0
        
        # 考虑关键,跨过n需要的最小代价->len(cost) + 1
        for i in range(2,len(cost)+1):
            dp[2] = min(dp[1] + cost[i-1], dp[0] + cost[i-2])
            dp[0] = dp[1]
            dp[1] = dp[2]
        
        return dp[2]
