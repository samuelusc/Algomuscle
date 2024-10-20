class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def find_above(x):
            return sum(num <= x for num in nums) > x
        
        left,right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if find_above(mid):
                right = mid
            
            else:
                left = mid + 1

        
        return left