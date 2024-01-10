class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # brute force
        len_nums = len(nums)
        i = 0
        # 这里要用while 而不是for
        while (i < len_nums):
            if nums[i] == val:               
                for j in range(i,len_nums - 1):
                    nums[j] = nums[j+1]               
                len_nums -= 1
            # 需要重新检查移动过来的i
            else:
                i += 1

        return len_nums