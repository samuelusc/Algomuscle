class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,sum_all,max_len = 0, 0, len(nums)+1

        for right in range(len(nums)):
            sum_all += nums[right]
            
            while sum_all >= target:
                max_len = min(max_len, right - left + 1)
                sum_all -= nums[left]
                left += 1
        

        return max_len if max_len <= len(nums) else 0
