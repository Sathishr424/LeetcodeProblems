# Last updated: 10/9/2025, 2:47:40 am
cmax = lambda x, y: x if x > y else y

@cache
def getTwo(num: int) -> int:
    cnt = 0
    while num % 2 == 0:
        cnt += 1
        num //= 2
    return cnt

def getFive(num):
    cnt = 0
    while num % 5 == 0:
        cnt += 1
        num //= 5
    return cnt

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        converted = [[[0, 0] for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                converted[i][j] = [getTwo(grid[i][j]), getFive(grid[i][j])]

        prefix_h2 = [[0] * n for _ in range(m)]
        prefix_v2 = [[0] * n for _ in range(m)]

        prefix_h5 = [[0] * n for _ in range(m)]
        prefix_v5 = [[0] * n for _ in range(m)]

        for i in range(m):
            two = 0
            five = 0
            for j in range(n):
                two += converted[i][j][0]
                five += converted[i][j][1]
                prefix_h2[i][j] = two
                prefix_h5[i][j] = five
        
        for j in range(n):
            two = 0
            five = 0
            for i in range(m):
                two += converted[i][j][0]
                five += converted[i][j][1]
                prefix_v2[i][j] = two
                prefix_v5[i][j] = five

        max_zero = 0

        for i in range(m):
            for j in range(n):
                v2 = prefix_v2[i][j] - converted[i][j][0]
                h2 = prefix_h2[i][j]

                v5 = prefix_v5[i][j] - converted[i][j][1]
                h5 = prefix_h5[i][j]

                v2_ = prefix_v2[-1][j] - v2
                h2_ = prefix_h2[i][-1] - h2
                v5_ = prefix_v5[-1][j] - v5
                h5_ = prefix_h5[i][-1] - h5

                two = converted[i][j][0]
                five = converted[i][j][1]

                max_zero = cmax(max_zero, min(v2 + h2, v5 + h5))
                max_zero = cmax(max_zero, min(v2_ + h2_, v5_ + h5_))
                max_zero = cmax(max_zero, min(v2 + h2_ + two, v5 + h5_ + five))
                max_zero = cmax(max_zero, min(v2_ + h2 - two, v5_ + h5 - five))
        
        return max_zero