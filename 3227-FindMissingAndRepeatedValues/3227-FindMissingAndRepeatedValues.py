# Last updated: 12/6/2025, 5:36:00 am
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        tot = (n*n+1)

        arr = [0] * tot

        for i in range(n):
            for j in range(n):
                arr[grid[i][j]] += 1

        ret = [0, 0]
        
        for i in range(1, tot):
            if arr[i] == 0:
                ret[1] = i
                if ret[0]: break
            elif arr[i] == 2:
                ret[0] = i
                if ret[1]: break
        
        return ret