498. Diagonal Traverse
# Approach: Simulation using direction toggle
# Time Complexity: O(n * m), where n = rows, m = cols
# Space Complexity: O(1) (excluding output list)

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)         # number of rows
        m = len(mat[0])      # number of columns
        x = y = 0            # starting point
        ok = False           # toggle for direction
        ans = []             # result array
        
        while x < n and y < m:
            if ok:  # Traverse bottom-left
                while y >= 0 and x < n:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
                if x >= n:   # adjust if row index goes out
                    x -= 1
                    y += 1
                y += 1       # move right
                ok = not ok  # flip direction
            else:  # Traverse top-right
                while x >= 0 and y < m:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1
                if y >= m:   # adjust if col index goes out
                    y -= 1
                    x += 1
                x += 1       # move down
                ok = not ok  # flip direction
        
        return ans
