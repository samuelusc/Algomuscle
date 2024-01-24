class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def backtracking(candidates, target, current_sum, startIndex):

            if current_sum == target:
                res.append(path[:])
                return

            for i in range(startIndex, len(candidates)):
                current_sum += candidates[i]
                if current_sum > target: 
                    break

                path.append(candidates[i])
                # 注意这里是i, 因为元素可以重复使用
                backtracking(candidates, target, current_sum, i)
                
                # sum 减去最后的candidate
                current_sum -= candidates[i]
                path.pop()

        backtracking(candidates, target, 0, 0) 

        return res