class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # 增加覆盖范围
        cover, i = 0, 0

        # 考虑只有一个元素情况
        if len(nums) == 1:
            return True

        # cover 代表 index,下面没有包括nums 只一个元素情况
        # should consider if i is over the boundary of len(nums)
        while i < len(nums) and i <= cover:
            cover = max(nums[i]+ i, cover)
            if cover >= len(nums) - 1:
                return True

            i += 1

        return False
