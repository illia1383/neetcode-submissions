class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res += 4
                    if r > 0 and grid[r - 1][c] == 1:
                        res -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        res -= 2
        return res 
                    