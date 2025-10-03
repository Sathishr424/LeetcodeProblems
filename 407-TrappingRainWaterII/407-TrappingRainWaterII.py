# Last updated: 3/10/2025, 9:48:01 am
class Solution:
    def trapRainWater(self, height: List[List[int]]) -> int:
        m = len(height)
        n = len(height[0])
        
        heap = []
        for i in range(m):
            heap.append((height[i][0], i, 0))
            heap.append((height[i][n-1], i, n-1))
            height[i][0] = -1
            height[i][n-1] = -1
        
        for i in range(1, n-1):
            heap.append((height[0][i], 0, i))
            heap.append((height[m-1][i], m-1, i))
            height[0][i] = -1
            height[m-1][i] = -1
        
        heapq.heapify(heap)

        DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        max_level = -1
        area = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            max_level = max(max_level, h)
            area += max_level - h

            for i2, j2 in DIR:
                i2 += i
                j2 += j
                if 0 <= i2 < m and 0 <= j2 < n and height[i2][j2] != -1:
                    heapq.heappush(heap, (height[i2][j2], i2, j2))
                    height[i2][j2] = -1
                
        return area