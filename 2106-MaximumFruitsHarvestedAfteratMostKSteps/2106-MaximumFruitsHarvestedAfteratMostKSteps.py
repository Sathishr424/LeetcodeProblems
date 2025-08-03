# Last updated: 3/8/2025, 12:51:13 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)

        prefix = [0]
        position = []

        for p, f in fruits:
            prefix.append(prefix[-1] + f)
            position.append(p)
        
        ret = 0
        for pos in range(cmax(0, startPos - k), startPos + 1):
            rem = k - (startPos - pos)
            left = bisect_left(position, pos)
            mid = bisect_left(position, startPos + 1)
            right = cmax(mid, bisect_left(position, pos + rem + 1))

            tot = prefix[right] - prefix[left]
            ret = cmax(ret, tot)

        for pos in range(startPos, startPos + k + 1):
            rem = k - (pos - startPos)
            left = bisect_left(position, pos - rem)
            mid = bisect_left(position, startPos + 1)
            right = cmax(mid, bisect_left(position, pos + 1))

            tot = prefix[right] - prefix[left]
            ret = cmax(ret, tot)
        
        return ret