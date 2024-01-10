class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left is included and right is include

        left, right = 0, len(nums) - 1
        
        # 保持循环不变量
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            
            elif nums[mid] > target:
                # 闭空间 -1
                right = mid - 1 

            else:
                return mid

        return -1  
                
