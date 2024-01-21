class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path, res = [], []
        def backtracking(n,k, start_index):
            if len(path) == k:
                res.append(path[:])
                return 
            

            for i in range(start_index, n - (k-len(path)) + 2):
                path.append(i)

                # 不是 start_index + 1,是当前i + 1
                backtracking(n,k, i + 1) 
                path.pop()
        
        backtracking(n,k,1)
        return res
