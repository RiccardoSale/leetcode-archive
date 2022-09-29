# Given an m x n 2D binary grid grid which represents
# a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r = len(grid)
        c = len(grid[0])
        res = 0

        dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # array for directions

        def dfs(x, y):
            if grid[x][y] == '1':  # if the value is one expand the dfs else stop it
                grid[x][y] = '_'
            else:
                return
            for dr, dc in dire:
                if 0 <= r + dr < r and 0 <= y + dc < c:
                    dfs(x + dr, y + dc)

        for x in range(r):  # check element that is equal than 1 and in "different tile"
            for y in range(c):
                if grid[x][y] == '1':
                    dfs(x, y)
                    res += 1
        return res
