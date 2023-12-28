class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left,right,end = 0,len(nums)-1,len(nums)-1
        res = [0] * len(nums) 

        while left <= right:
            if nums[left]**2 >= nums[right]**2:
                res[end] = nums[left]**2
                left += 1
                end -= 1
            else:
                res[end] = nums[right]**2
                right -= 1
                end -= 1
        
        return res

