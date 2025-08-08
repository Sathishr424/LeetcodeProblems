# Last updated: 9/8/2025, 4:10:46 am
# [[1, 5, 9],
#  [10,11,14],
#  [12,13,15]]

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        l = matrix[0][0]
        r = matrix[n-1][n-1]

        def smallest(num):
            count = 0
            for i in range(n):
                if matrix[i][n-1] <= num:
                    count += n
                else:
                    count += bisect_right(matrix[i], num)
            return count

        while l < r:
            mid = (l + r) // 2
            if smallest(mid) < k:
                l = mid + 1
            else:
                r = mid
        
        return l