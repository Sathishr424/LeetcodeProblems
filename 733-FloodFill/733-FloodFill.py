# Last updated: 12/6/2025, 5:47:18 am
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        curr = image[sr][sc]
        if curr == color: return image
        def dfs(i, j):
            if i < 0 or j < 0 or i == m or j == n or image[i][j] != curr: return
            image[i][j] = color
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        dfs(sr, sc)
        return image
        