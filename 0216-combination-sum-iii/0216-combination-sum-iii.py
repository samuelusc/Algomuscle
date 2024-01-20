class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.path = []
        self.res = []

        self.backtracking(k,n,0,1)
        return self.res
        
    def backtracking(self, k,n, sumAll, startIndex):
        if len(self.path) == k:
            if sumAll == n:
                self.res.append(self.path[:])
            #只要元素到达k，无论是否n都停止继续递归
            return 
        


        for i in range(startIndex, 10):
            sumAll += i
            # 减枝 prune invalid if samAll > n
            if sumAll > n:
                continue
            self.path.append(i)

            self.backtracking(k,n,sumAll, i + 1)

            sumAll -= i
            self.path.pop()
            