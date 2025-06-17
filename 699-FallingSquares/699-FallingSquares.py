# Last updated: 17/6/2025, 10:29:11 am
class Solution:
    def fallingSquares(self, pos: List[List[int]]) -> List[int]:
        n = len(pos)
        ret = []

        plane = SortedList()

        def collision(left, right):
            if left[0] > right[0]:
                left, right = right, left
            # print(left, right)
            if right[0] >= left[0] and right[0] < left[1]:
                return True
            
            return False

        max_height = 0
        for i in range(n):
            height = pos[i][1]
            for j in range(len(plane)):
                if collision((pos[i][0], pos[i][0] + pos[i][1]), plane[j]):
                    # print('collision', plane[j], pos[i])
                    height = max(height, plane[j][2] + pos[i][1])
            
            max_height = max(max_height, height)
            plane.add((pos[i][0], pos[i][0] + pos[i][1], height))
            # print(plane, height)
            ret.append(max_height)
        
        return ret