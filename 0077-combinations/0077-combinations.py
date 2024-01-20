class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path,res = [],[]

        def backtracking(n, k, index_start):
            if len(path) == k:
                res.append(path[:])
                return

            
            for i in range(index_start, n+1):
                path.append(i)
                
                backtracking(n,k, i + 1)

                path.pop()

        
        backtracking(n,k, 1)
        return res
