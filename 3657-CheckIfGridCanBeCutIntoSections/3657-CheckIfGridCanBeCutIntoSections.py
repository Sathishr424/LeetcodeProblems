# Last updated: 12/6/2025, 5:35:08 am
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontal = True
        vertical = True
        half = n-2

        for x1, y1, x2, y2 in rectangles:
            if x2-x1 > half:
                vertical = False
            if y2-y1 > half:
                horizontal = False
        
        if horizontal:
            rectangles.sort(key=lambda x: x[1])
            prev = (rectangles[0][1], rectangles[0][3])
            cuts = 0
            for i in range(1, len(rectangles)):
                _, y1, _, y2 = rectangles[i]

                if y1 < prev[1]:
                    prev = (prev[0], max(prev[1], y2))
                else:
                    prev = (y1, y2)
                    # print('hori', prev)
                    cuts += 1
                    if cuts == 2: return True
        if vertical:
            rectangles.sort(key=lambda x: x[0])
            prev = (rectangles[0][0], rectangles[0][2])
            cuts = 0
            for i in range(1, len(rectangles)):
                x1, _, x2, _ = rectangles[i]

                if x1 < prev[1]:
                    prev = (prev[0], max(prev[1], x2))
                else:
                    prev = (x1, x2)
                    # print('vert', prev)
                    cuts += 1
                    if cuts == 2: return True
        return False