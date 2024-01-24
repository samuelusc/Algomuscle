class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        nums.sort()

        def backtracking(nums, startIndex):
            res.append(path[:])

            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                
                backtracking(nums, i + 1)

                path.pop()
        

        backtracking(nums, 0)
        return res
