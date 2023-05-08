class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sumOfElements = 0
        
        for i in range(n):
            sumOfElements += mat[i][i]
            sumOfElements += mat[n-1-i][i]
        if n%2 != 0:
            sumOfElements -= mat[n//2][n//2]
        return sumOfElements
        