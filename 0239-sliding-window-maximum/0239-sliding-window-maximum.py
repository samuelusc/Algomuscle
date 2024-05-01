from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = [] 

        for i in range(len(nums)):

            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            if queue[0] <= i - k:
                queue.popleft()
            
            if i + 1 -k >= 0:
                res.append(nums[queue[0]])
        
        return res
