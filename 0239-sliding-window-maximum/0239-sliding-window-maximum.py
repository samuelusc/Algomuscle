from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        res = []
        for index, val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                stack.pop()

            stack.append(index)

            if stack and stack[0] < index + 1 - k:
                stack.popleft()
            
            if index + 1 >= k:
                res.append(nums[stack[0]])

        return res