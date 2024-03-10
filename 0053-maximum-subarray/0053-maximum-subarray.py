class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = dp[0]

        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

            if res < dp[i]:
                res = dp[i]

        return res