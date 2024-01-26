class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(nums, startIndex):
            if len(path) > 1:
                res.append(path[:])


            seen = set()

            for i in range(startIndex, len(nums)):
                if (path and nums[i] < path[-1]) or nums[i] in seen:
                    continue
                seen.add(nums[i])
                path.append(nums[i])

                backtracking(nums, i + 1)    
                path.pop()


        backtracking(nums, 0)     
        return res
