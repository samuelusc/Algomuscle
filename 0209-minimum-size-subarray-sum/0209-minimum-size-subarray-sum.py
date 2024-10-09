class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, count = 0, 0
        minl = float('inf')

        for r in range(len(nums)):
            count += nums[r]

            while left <= r and count >= target:
                minl = min(minl, r - left + 1)
                count -= nums[left]
                left += 1
        
        return minl if minl != float('inf') else 0
