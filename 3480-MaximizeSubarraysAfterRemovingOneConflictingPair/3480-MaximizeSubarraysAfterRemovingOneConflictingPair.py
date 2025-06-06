# Last updated: 7/6/2025, 3:02:25 am
class Solution:
    def maxSubarrays(self, n: int, cp: List[List[int]]) -> int:
        m = len(cp)

        for i, (x, y) in enumerate(cp):
            if x > y:
                cp[i][0], cp[i][1] = cp[i][1], cp[i][0]

        cp.sort()
        better = [0] * m

        start = [x for x, _ in cp]
        end = deque([])

        cp.append([0, n+1])

        sl = [m-1, m]
        end.appendleft(sl + [])

        for i in range(m-2, -1, -1):
            if cp[i][1] <= cp[sl[0]][1]:
                sl[1] = sl[0]
                sl[0] = i
            elif cp[i][1] < cp[sl[1]][1]:
                sl[1] = i
            
            end.appendleft(sl + [])

        cnt = 0
        for i in range(n, 0, -1):
            index = bisect_left(start, i)
            if index < m:
                index_2 = end[index][0]
                diff = cp[index_2][1] - i
                cnt += diff
                better[index_2] += (cp[ end[index][1] ][1] - i) - diff
            else:
                cnt += n-i+1
        
        return cnt + max(better)