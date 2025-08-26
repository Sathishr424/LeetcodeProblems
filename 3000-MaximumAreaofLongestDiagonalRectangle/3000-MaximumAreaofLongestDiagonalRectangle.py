# Last updated: 26/8/2025, 10:39:32 am
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_diagonal = 0
        for i, (l, w) in enumerate(dimensions):
            s = sqrt(l * l + w * w)
            if s > max_diagonal or (s == max_diagonal and l * w > dimensions[max_area][0] * dimensions[max_area][1]):
                max_diagonal = s
                max_area = i
        
        return dimensions[max_area][0] * dimensions[max_area][1]