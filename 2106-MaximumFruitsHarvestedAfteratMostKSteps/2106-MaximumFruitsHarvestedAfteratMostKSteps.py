# Last updated: 3/8/2025, 12:26:39 pm
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)

        prefix = [0]
        position = []

        for p, f in fruits:
            prefix.append(prefix[-1] + f)
            position.append(p)
        
        # print(prefix)
        
        ret = 0
        for pos in range(max(0, startPos - k), startPos + 1):
            rem = k - (startPos - pos)
            left = bisect_left(position, pos)
            mid = bisect_left(position, startPos + 1)
            right = max(mid, bisect_left(position, pos + rem + 1))

            tot = prefix[right] - prefix[left]
            # print(pos, fruits[left:right], sum([x[1] for x in fruits[left:right]]), tot, rem)
            ret = max(ret, tot)
        # print('---')
        for pos in range(startPos, startPos + k + 1):
            rem = k - (pos - startPos)
            left = bisect_left(position, pos - rem)
            mid = bisect_left(position, startPos + 1)
            right = max(mid, bisect_left(position, pos + 1))

            tot = prefix[right] - prefix[left]
            # print(pos, fruits[left:right], sum([x[1] for x in fruits[left:right]]), tot, rem)
            ret = max(ret, tot)
        
        # print(ret)
        return ret

# [[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]]