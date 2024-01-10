class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left is included and right is excluded

        left, right = 0, len(nums)
        # 保持循环不变量
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            
            elif nums[mid] > target:
                # Notice here it's not mid - 1
                right = mid 

            else:
                return mid

        return -1  
                
