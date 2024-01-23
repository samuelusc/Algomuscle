class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        path = []
        

        def backtracking(str, startIndex):
            if startIndex == len(str):
                res.append(path[:])
                return

            for i in range(startIndex, len(s)):
                check_s = s[startIndex : i+1]
                if check_s == check_s[::-1]:
                    path.append(check_s)

                else:
                    continue

                backtracking(s, i + 1)
                path.pop()
            
        backtracking(s,0)
        return res
        



               

