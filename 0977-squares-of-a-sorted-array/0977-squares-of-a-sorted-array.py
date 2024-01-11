class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #two pointers

        left, right, end = 0, len(nums) - 1, len(nums) -1
        res = [0] * len(nums)

        # 观察知道最大数要么是最左边的平方，要么最右边的平方
        # 对新数组赋值从后往前
        while left <= right:
            if nums[left]**2 >= nums[right]**2:
                res[end] = nums[left] ** 2 
                
                end -= 1
                left += 1
            
            else:
                res[end] = nums[right] ** 2

                end -= 1
                right -= 1
        
        return res