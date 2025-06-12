# Last updated: 12/6/2025, 5:53:57 am
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m*n-1
        while left <= right:
            mid = (left+right)//2

            i = mid // n
            j = mid % n

            if matrix[i][j] < target:
                left = mid+1
            elif matrix[i][j] > target:
                right = mid-1
            else:
                return True
        
        return False