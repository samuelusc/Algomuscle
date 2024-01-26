class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        path = []
        res = []
        visited = [False] * len(nums)
        nums.sort()
        def backtracking(nums, visited):
            if len(path) == len(nums):
                print(path)
                res.append(path[:])
                return 


            for i in range(0, len(nums)):
                # 去重逻辑1，树枝去重 3个条件
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                # 去重逻辑2，树叶去重            
                if visited[i]:
                    continue

                visited[i] = True
                path.append(nums[i])

                backtracking(nums, visited)
                visited[i] = False
                path.pop()

        backtracking(nums, visited)
        return res
