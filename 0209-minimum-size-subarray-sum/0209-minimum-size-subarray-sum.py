class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        minL,curSum = float('inf'), 0

        for j in range(len(nums)):
            curSum += nums[j]
            while curSum >= target:
                minL = min(minL, j-i+1)
                curSum -= nums[i]
                i+=1
                
            
        return minL if minL != float('inf') else 0
