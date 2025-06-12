# Last updated: 12/6/2025, 5:39:06 am
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n = len(grid[0])
        m = len(grid)

        arr = []

        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])
        
        arr.sort()

        mid = arr[len(arr)//2]
        ret = 0
        for num in arr:
            diff = abs(num-mid)
            if diff // x != diff / x: return -1
            ret += diff // x

        return ret