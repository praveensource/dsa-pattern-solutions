1572.Matrix Diagonal Sum

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Approach 1 (❌ Wrong if values repeat):
        - Using a set to store diagonal elements avoids double counting
          of the middle element in odd-sized matrices.
        - But this is incorrect because sets ignore duplicate values.
          Example: if all elements are 1, result will be wrong.
        """

        # ans = set()
        # m, n = len(mat), len(mat[0])
        # i, j = 0, 0
        # while i < m and j < n:
        #     ans.add(mat[i][j])
        #     i += 1
        #     j += 1
        #
        # k, l = 0, n - 1
        # while k < m and l >= 0:
        #     ans.add(mat[k][l])
        #     k += 1
        #     l -= 1
        #
        # return sum(ans)   # ❌ Wrong in cases like all ones


        """
        Approach 2 (✅ Correct and Optimal):
        - Traverse both diagonals in a single loop.
        - Add primary (i, i) and secondary (i, n-i-1).
        - If n is odd, subtract the middle element (counted twice).
        Time: O(n)
        Space: O(1)
        """

        total = 0
        n = len(mat)
        for i in range(n):
            total += mat[i][i]             # primary diagonal
            total += mat[i][n - i - 1]     # secondary diagonal

        if n % 2 == 1:                     # subtract middle element (counted twice)
            total -= mat[n // 2][n // 2]

        return total
