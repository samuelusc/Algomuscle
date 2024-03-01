class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        


        def helper(nums, start, end):
            if start == end:
                return nums[start]
            
            pre = nums[start]
            cur = max(nums[start],nums[start + 1])

            for i in range(start + 2, end + 1):
                temp = cur
                cur = max(pre + nums[i], temp)
                pre = temp
            
            return cur
           
        
        res = max(helper(nums, 0, len(nums) -2), helper(nums, 1, len(nums)-1))
        return res


    