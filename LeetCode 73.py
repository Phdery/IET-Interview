from typing import List


def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        column = len(matrix[0])
        index_row = []
        index_col = []

        # Find the index
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    index_row.append(i)
                    index_col.append(j)
        print(index_row, index_col)

        # Set the row and column to 0 according to the index
        for i in range(row):
            for j in range(column):   
                if i in index_row or j in index_col:
                    matrix[i][j] = 0


matrix: List[List[int]] = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
setZeroes(matrix, matrix)
print("The final result should be: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]")
print("The final result is:", matrix)