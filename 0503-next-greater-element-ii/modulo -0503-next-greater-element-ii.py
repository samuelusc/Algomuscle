class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = [0]

        for i in range(1, len(nums) * 2):
            index = i % len(nums)

            while stack and nums[index] > nums[stack[-1]]:
                res[stack[-1]] = nums[index]
                stack.pop()
            
            stack.append(index)
        
        return res
