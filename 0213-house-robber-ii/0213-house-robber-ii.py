class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        


        def helper(new_nums):
            if len(new_nums) < 2:
                return new_nums[0]

            dp = [0] * len(new_nums)    
            dp[0] = new_nums[0]
            dp[1] = max(new_nums[0],new_nums[1])

            for i in range(2, len(new_nums)):
                dp[i] = max(dp[i-1],dp[i-2] + new_nums[i])
            
            return dp[-1]
        
        res = max(helper(nums[1:]), helper(nums[:-1]))
        return res


    