class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[n]]

        row = col = index = 0
        dire = [(0,1),(1,0),(0,-1),(-1,0)]
        s = [[0] * n for _ in range(n)]

        for i in range(1, n*n + 1):
            s[row][col] = i

            x,y = dire[index]
            row_next, col_next = row+x, col+y

            if not 0<=row_next<n or not 0<=col_next<n or s[row_next][col_next] != 0:
                index = (index + 1) % 4
                x,y = dire[index]
                row_next, col_next = row + x, col + y
            
            row, col = row_next, col_next
        
        return s


