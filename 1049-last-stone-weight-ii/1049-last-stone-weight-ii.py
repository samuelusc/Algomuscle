class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        target = sum(stones) // 2
        dp = [0] * (target + 1)

        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = max(dp[j], dp[j-stone] + stone)

        res = sum(stones) - 2 * dp[target]

        return res