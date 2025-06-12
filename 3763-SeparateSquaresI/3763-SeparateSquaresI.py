# Last updated: 12/6/2025, 5:34:34 am
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        n = len(squares)
        left = 0
        right = 0

        for x, y, l in squares:
            left = min(y, left)
            right = max(y+l, right)
        
        precision = 1 / (10**5)
        while right - left > precision:
            mid = (left+right) / 2

            top = 0
            bottom = 0

            for x, y, l in squares:
                if y < mid and y+l > mid:
                    b = mid-y
                    t = l - b
                    top += t * l
                    bottom += b * l
                elif y < mid:
                    bottom += l*l
                else:
                    top += l*l
            
            if top > bottom:
                left = mid
            else:
                right = mid

        return left