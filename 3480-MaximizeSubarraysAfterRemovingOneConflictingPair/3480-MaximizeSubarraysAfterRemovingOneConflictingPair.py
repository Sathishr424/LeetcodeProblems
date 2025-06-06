# Last updated: 7/6/2025, 2:51:18 am
class Solution:
    def maxSubarrays(self, n: int, cp: List[List[int]]) -> int:
        m = len(cp)

        for i, (x, y) in enumerate(cp):
            if x > y:
                cp[i][0], cp[i][1] = cp[i][1], cp[i][0]

        cp.sort()
        # print(cp)
        better = [0] * m

        start = [x for x, _ in cp]
        
        end = deque([])
        end.append(m-1)
        secondEnd = deque([])
        secondEnd.append(n+1)

        sl = [cp[-1][1], n+1]

        for i in range(len(cp)-2, -1, -1):
            if cp[i][1] < cp[end[0]][1]:
                end.appendleft(i)
            else:
                end.appendleft(end[0])
            
            if cp[i][1] <= sl[0]:
                sl[1] = sl[0]
                sl[0] = cp[i][1]
            elif cp[i][1] < sl[1]:
                sl[1] = cp[i][1]
            
            # print(i, sl)
            secondEnd.appendleft(sl[1])
        
        # print(secondEnd)
        cnt = 0
        for i in range(n, 0, -1):
            index = bisect_left(start, i)
            if index < m:
                index_2 = end[index]
                diff = cp[index_2][1] - i
                cnt += diff
                better[index_2] += (secondEnd[index] - i) - diff
            else:
                cnt += n-i+1
        
        return cnt + max(better)