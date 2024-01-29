class Solution:
    def jump(self, nums: List[int]) -> int:
        
        last, cover, count = 0, 0, 0

        for i in range(len(nums) - 1):
            cover = max(cover, nums[i] + i)

            if i == last:
                count += 1
                last = cover

        return count