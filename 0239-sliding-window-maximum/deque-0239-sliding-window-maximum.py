from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:       
        # initialize deque
        queue = deque()
        res = []
        #acquire each index and value by iterating through nums
        for i, num in enumerate(nums):
            
            # Notice not "if" here, 
            # we iterately remove every numbers in the queue,
            # that is less than the current one before it 
            while queue and num >= nums[queue[-1]]:
                queue.pop()
            # Notice! push current index into queue
            queue.append(i)
            #remove the first ele if it's outside the window
            if queue[0] == i - k:
                queue.popleft()
            # check if the length at the current position has
            # reached the required window size
            if i + 1 >= k:
                res.append(nums[queue[0]])

        return res

                
