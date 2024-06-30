class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,columns = len(matrix),len(matrix[0])

        left, right = 0, rows * columns - 1

        while left < right: 
            mid = (left + right) // 2
            row, column = divmod(mid, columns)

            if matrix[row][column] >= target:
                right = mid
            else:
                left = mid + 1
        
        return matrix[left // columns][left % columns] == target

