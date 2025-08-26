# Last updated: 26/8/2025, 10:46:33 am
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_diagonal = 0
        for i, (l, w) in enumerate(dimensions):
            s = l * l + w * w
            area = l * w
            if s > max_diagonal or (s == max_diagonal and area > max_area):
                max_diagonal = s
                max_area = area
        
        return max_area