class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 排序让相邻元素在一起
        # 树层去重，树枝不去重

        candidates.sort()
        res = []
        path = []

        def backtracking(candidates, target, current_sum, startIndex):
            if current_sum == target:
                res.append(path[:])

            
            for i in range(startIndex, len(candidates)):
                #检查相邻的两个是否相等
                if i > startIndex and candidates[i] == candidates[i-1]:
                    continue
                # 求合
                current_sum += candidates[i]
                # pruning branches
                if current_sum > target:
                    break
                
                path.append(candidates[i])
                backtracking(candidates, target, current_sum, i + 1)
                current_sum -= candidates[i]
                path.pop()

        backtracking(candidates, target, 0, 0)

        return res