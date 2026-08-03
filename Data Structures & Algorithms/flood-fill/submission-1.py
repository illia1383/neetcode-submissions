class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_col = image[sr][sc]
        if starting_col == color:
            return image
        def dfs(r,c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != starting_col:
                return 
            image[r][c] = color
            dfs(r + 1 , c)
            dfs(r - 1, c)
            dfs(r , c + 1)
            dfs(r , c - 1)
        
        
        dfs(sr,sc)
        return image
        
