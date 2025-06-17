# Last updated: 17/6/2025, 12:44:12 pm
class Solution:
    def fallingSquares(self, pos: List[List[int]]) -> List[int]:
        n = len(pos)
        ret = []

        plane = SortedList()

        def collision(left, right):
            if left[0] > right[0]:
                left, right = right, left

            if right[0] >= left[0] and right[0] < left[1]:
                return True
            
            return False

        max_height = 0
        for i in range(n):
            height = pos[i][1]
            index = plane.bisect_left((pos[i][0] + pos[i][1], 0, 0))
            for j in range(min(len(plane)-1, index), -1, -1):
                if collision((pos[i][0], pos[i][0] + pos[i][1]), plane[j]):
                    height = max(height, plane[j][2] + pos[i][1])
            
            max_height = max(max_height, height)
            plane.add((pos[i][0], pos[i][0] + pos[i][1], height))
            ret.append(max_height)
        
        return ret