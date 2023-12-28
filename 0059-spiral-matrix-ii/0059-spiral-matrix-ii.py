class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        
        row, col, index = 0,0,0
        directions = ((0,1),(1,0),(0,-1),(-1,0))
        matrix = [[0]* n for _ in range (n)]
        
        for value in range(1,n*n+1):
            
            matrix[row][col] = value
            
            x, y = directions[index]
            row_next, col_next = row + x, col + y

            if not 0 <= row_next < n or not 0 <= col_next < n or matrix[row_next][col_next] != 0:
                index = (index +1) % 4

            x,y = directions[index]

            row, col = row + x, col + y
        
        return matrix