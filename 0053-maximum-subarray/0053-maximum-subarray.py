class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initialization
        dp = [0] * len(nums)
        
        #base case
        dp[0] = nums[0]

        res = dp[0]
        
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            print(dp[i])
            if dp[i] > res:
                res = dp[i]

        return res 