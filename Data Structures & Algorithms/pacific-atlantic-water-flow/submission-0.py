class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## 4 directions, to neighbour cell with height equal or lower
        ## Water goes into ocean from adjacent cells 

        ##Goal: find all cells where water can flow from that cell to each ocean 

        ROWS,COLS = len(heights), len(heights[0])

        pac,atl = set(),set()


        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or 
                r < 0 or c < 0 or r == ROWS or c == COLS or 
                heights[r][c] < prevHeight):
                    return 

            ##Add it to the visit set        
            visit.add((r,c))
            #The 4 directions
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            
        #For the first ROW which is adjacent to the Pacific and Atlantic
        for c in range(COLS):
            dfs(0,c,pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        #For the first COL which is adjacent ot the Pacific and Atlantic
        for r in range(ROWS):
            dfs(r,0,pac, heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS- 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res 

