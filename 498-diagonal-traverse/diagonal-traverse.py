class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        row, col = 0, 0
        rows, cols = len(mat), len(mat[0])
        for _ in range(rows * cols):
            result.append(mat[row][col])
            if (row + col) % 2 == 0:
                if col == cols - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            else:
                if row == rows - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1

        return result

