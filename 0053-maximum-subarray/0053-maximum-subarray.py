class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = float('-inf')
        count = 0

        for num in nums:
            count += num

            res = max(count, res)

            if count < 0:
                count = 0

        return res