class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pre_diff = 0
        cur_diff = 0

        result = 1
        # 处理三种情况 1.上下有平坡
        # 2. 首位元素
        # 单调坡度平坡


        for i in range(len(nums)-1):
            cur_diff = nums[i+1] - nums[i]
            if (pre_diff >= 0 and cur_diff < 0) or (pre_diff <= 0 and cur_diff > 0):
                result += 1
                pre_diff = cur_diff
            #pre_diff = cur_diff 放在这里没有考虑单调平坡情况

        return result
