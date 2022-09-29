"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        r = len(heights)
        c = len(heights[0])

        dire = [[+1, 0], [-1, 0], [0, +1], [0, -1]]
        pacific = set()
        atlantic = set()
        #two set then we make the intersection
        #dfs from atlantic border and dfs from pacific border
        #heights[x][y] need to be >= as prec or we cant continue water dont flow
        def dfs(x, y, prec, set_):
            if x < 0 or x >= r or y < 0 or y >= c or (x, y) in set_ or heights[x][y] < prec:
                return
            else:
                set_.add((x, y)) #we add to the set each element so we dont enter more than one time
                for dr, dc in dire:
                    dfs(x + dr, y + dc, heights[x][y], set_)

        for x in range(r):
            dfs(x, 0, heights[x][0], pacific)
            dfs(x, c - 1, heights[x][c - 1], atlantic)

        for y in range(c):
            dfs(0, y, heights[0][y], pacific)
            dfs(r - 1, y, heights[r - 1][y], atlantic)

        res = []
        for x in range(r):
            for y in range(c):
                if (x, y) in pacific and (x, y) in atlantic:
                    res.append([x, y])

        #or we can do return list(pacific.intersection(atlantic))
        return res