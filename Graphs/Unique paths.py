class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        data = [[1 for x in range(n)] for y in range(m)]
        # lista di n colonne per tot righe
        # list of n columns x number of rows (m)
        for x in range(1, m):
            for y in range(1, n):
                data[x][y] = data[x - 1][y] + data[x][y - 1]
        return data[m - 1][n - 1]
