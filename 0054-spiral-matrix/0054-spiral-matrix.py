class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        index, row, col = 0,0,0
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(m*n):
            
            res.append(matrix[row][col])
            visited.add((row,col))

            next_row,next_col = row + directions[index][0], col + directions[index][1]
            if not 0 <= next_row < m or not 0 <= next_col < n or (next_row,next_col) in visited:
                index = (index + 1) % 4

            row += directions[index][0]
            col += directions[index][1]

        return res