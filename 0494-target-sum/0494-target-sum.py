class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if total_sum < abs(target) or (total_sum + target) % 2 != 0:
            return 0

        sub = (total_sum + target) // 2

        dp = [[0] * (sub + 1) for _ in range (len(nums) + 1)]


        dp[0][0] = 1

        for i in range (1, len(nums) + 1):
            for j in range(sub + 1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] += dp[i-1][j-nums[i-1]]

        
        return dp[-1][sub]