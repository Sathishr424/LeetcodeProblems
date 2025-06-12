# Last updated: 12/6/2025, 5:42:29 am
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        ret = 0
        yet_to_open = [0] * n
        opened = [0] * n

        def openBox(box):
            if opened[box]: return 0
            if status[box] == 1:
                ans = candies[box]
                opened[box] = 1

                for b in keys[box]:
                    status[b] = 1
                    if yet_to_open[b]:
                        ans += openBox(b)

                for b in containedBoxes[box]:
                    ans += openBox(b)
                return ans
            else:
                yet_to_open[box] = 1
                return 0

        for box in initialBoxes:
            ret += openBox(box)
        
        return ret



