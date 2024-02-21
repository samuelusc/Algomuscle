class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        if total < abs(target) or ((total + target) % 2 != 0):
            return 0

        bag_size = (total + target)//2
        dp = [[0]*(bag_size+1) for _ in range(len(nums))]

        dp[0][0] = 2 if nums[0] == 0 else 1
        for j in range(1, bag_size+1):
            if nums[0] == j:
                dp[0][j] = 1

        for j in range(bag_size + 1):
            for i in range(1, len(nums)):
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]