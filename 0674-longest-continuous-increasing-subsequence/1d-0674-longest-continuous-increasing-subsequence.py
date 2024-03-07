class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # initialzation
        dp = [1] * len(nums)
        # output
        res = 1
        # iterate through the list nums
        for i in range(1,len(nums)):
            # increasing subsequemnce
            if nums[i] > nums[i-1]:
                # continuous one 
                dp[i] = dp[i-1] + 1
            # assign the longest value to the output
            if res < dp[i]:
                res = dp[i]

        return res
            
