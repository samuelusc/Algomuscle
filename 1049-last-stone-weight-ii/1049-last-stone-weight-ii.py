class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        target = sum(stones) // 2


        dp = [0] * (target + 1)

        for num in stones:
            for j in range(target, num-1, -1):
                dp[j] = max(dp[j],dp[j-num]+ num)

        
        
        res = sum(stones) - 2 * dp[-1] 

        return res