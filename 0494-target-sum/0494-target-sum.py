class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        size = (total + target) // 2

        if abs(total) < abs(target) or (total + target) % 2 != 0:
            return 0

        dp = [0] * (size + 1)
        
        # Base case: one way to sum to 0 (using no numbers)
        dp[0] = 1 

        for num in nums:
            for j in range(size, num - 1, -1):          
                dp[j] += dp[j-num]
        

        return dp[-1]