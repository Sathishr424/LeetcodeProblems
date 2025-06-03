# Last updated: 3/6/2025, 11:37:29 am
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        opened = {}
        yet_to_open = {}

        def openBox(box):
            if box in opened: return
            if status[box] == 1:
                opened[box] = 1

                for b in keys[box]:
                    status[b] = 1
                    if b in yet_to_open:
                        openBox(b)

                for b in containedBoxes[box]:
                    openBox(b)
            else:
                yet_to_open[box] = 1

        for box in initialBoxes:
            openBox(box)

        ret = 0
        # print(opened)
        # print(yet_to_open)

        for box in opened:
            ret += candies[box]
        
        return ret



