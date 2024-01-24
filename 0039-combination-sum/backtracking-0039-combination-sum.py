class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(candidates, target, sum, startIndex):
            print(sum)
            if sum > target:
                return

            if sum == target:
                res.append(path[:])
                return

            for i in range(startIndex, len(candidates)):
                sum += candidates[i]

                path.append(candidates[i])
                # 注意这里是i, 因为元素可以重复使用
                backtracking(candidates, target, sum, i)
                
                # sum 减去最后的candidate
                sum -= candidates[i]
                path.pop()

        backtracking(candidates, target, 0, 0) 

        return res
