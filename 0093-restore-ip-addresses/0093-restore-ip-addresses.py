class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        def backtracking(startIndex):
            if startIndex >= len(s) and len(path)==4:
                res.append(".".join(path))
                return

            if len(path) > 4:
                return

            for i in range(startIndex, min(startIndex + 3, len(s))):
                if is_valid (startIndex, i):
                    path.append(s[startIndex: i + 1])
                    backtracking(i + 1)
                    path.pop()


        def is_valid(start, end):
            if s[start] == "0" and end!=start :
                return False
            
            return 0 <=int(s[start: end + 1]) <= 255

        
        backtracking(0)
        return res

       