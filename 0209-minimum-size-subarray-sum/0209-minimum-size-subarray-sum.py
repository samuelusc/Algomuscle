class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float("inf")
        left,total = 0,0

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                minlen = min(right - left + 1, minlen)
                total -= nums[left]
                left += 1
        
        return minlen if minlen != float("inf") else 0
                