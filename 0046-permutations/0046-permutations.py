class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 与combination question 不同在于树枝可以重复选取
        res = []
        path = []
        visited = [False] * len(nums)

        # 这里不用startIndex,因为可以重复选取
        # 只需要避免这次已经选过的即可
        def backtracking(nums,visited):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(0, len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                path.append(nums[i])

                backtracking(nums,visited)
                visited[i] = False
                path.pop()


        backtracking(nums,visited)
        return res