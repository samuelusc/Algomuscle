class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        
        matrix = [[0]* n for _ in range(n)]
        directions = ((0,1),(1,0),(0,-1),(-1,0))
        row, col,index = 0,0,0

        for value in range(1,n*n+1):
            
            matrix[row][col] = value            
            x,y = directions[index]
            next_row,next_col = row + x, col + y

            if not 0<= next_row < n or not 0 <= next_col < n or matrix[next_row][next_col] > 0:
                index = (index + 1) % 4
            
            x,y = directions[index]
            row,col = row + x, col + y
        
        return matrix