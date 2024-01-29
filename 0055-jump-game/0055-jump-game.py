class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        cover = 0

        for index, jump in enumerate(nums):
            # if max cover cannot reach index
            # just return False

            if cover < index:
                return False

            # pick up the longest cover jump
            cover = max(cover, index + jump)

        #never meet the case of False
        return True