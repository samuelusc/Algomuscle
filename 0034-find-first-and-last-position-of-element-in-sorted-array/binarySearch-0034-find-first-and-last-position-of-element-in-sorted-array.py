class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first,last = -1,-1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            
            else:
                left = mid + 1
        
        left, right = 0, len(nums) - 1
        while left <=right:
            mid = (left+right) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1
            
            else:
                left = mid + 1

        return (first, last)
