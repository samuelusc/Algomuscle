class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(nums, startIndex):
            # 这里是开始记录的条件，而不是递归结束条件
            if len(path) > 1:
                #结果在树枝和树叶
                res.append(path[:])
            # 为什么没有加return 因为会跳过后面的元素，而这里并非截止点

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
