class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
   
        rows = len(matrix)
        cols = len(matrix[0])

         # Step 1: Precompute max of each column
        col_max = [max(matrix[i][j] for i in range(rows)) for j in range(cols)]

        for i in range(rows):
            for j in range(cols):
                # we are looping and finding if it has -1 
                if matrix[i][j] == -1:
                    matrix[i][j] = col_max[j]
        return matrix
                    