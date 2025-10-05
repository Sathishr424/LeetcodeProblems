# Last updated: 5/10/2025, 10:46:56 am
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        visited = [[0] * n for _ in range(m)]
        stack = deque([])
        for j in range(n):
            visited[0][j] |= 1 << 0
            visited[m-1][j] |= 1 << 1
            stack.append([0, j, 0])
            stack.append([m-1, j, 1])
        for i in range(m):
            visited[i][0] |= 1 << 0
            visited[i][n-1] |= 1 << 1
            stack.append([i, 0, 0])
            stack.append([i, n-1, 1])
        
        while stack:
            i, j, ocean = stack.popleft()
            
            for i2, j2 in DIR:
                i2 += i
                j2 += j
                if 0 <= i2 < m and 0 <= j2 < n and heights[i2][j2] >= heights[i][j]:
                    if visited[i2][j2] & (1 << ocean) == 0:
                        stack.append([i2, j2, ocean])
                        visited[i2][j2] |= (1 << ocean)

        ret = []
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 3:
                    ret.append([i, j])
        
        return ret