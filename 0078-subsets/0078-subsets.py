class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []

        self.backtracking(nums, 0)
        return self.res



    def backtracking(self, nums, startIndex):
        
        # 如果最后递归为[1,2,3]，所以先放入再检查
        self.res.append(self.path[:])

        # 下面可以省略，因为 for循环已经帮助处理 startIndex > len(nums)
        # if startIndex >= len(nums):
        #     return
    

        for i in range(startIndex, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()
