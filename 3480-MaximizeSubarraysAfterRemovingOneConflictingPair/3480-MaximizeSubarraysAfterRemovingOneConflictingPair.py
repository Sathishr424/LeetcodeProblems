# Last updated: 7/6/2025, 2:36:29 am
class Solution:
    def maxSubarrays(self, n: int, cp: List[List[int]]) -> int:
        m = len(cp)

        for i, (x, y) in enumerate(cp):
            cp[i] = [min(x,y), max(x,y)]

        cp.sort()

        better = [0] * m

        start = [x for x, _ in cp]
        
        end = deque([])
        end.append(m-1)
        secondEnd = deque([])
        secondEnd.append(n+1)

        sl = SortedList()
        sl.add((cp[-1][1], m-1))

        for i in range(len(cp)-2, -1, -1):
            if cp[i][1] < cp[end[0]][1]:
                end.appendleft(i)
            else:
                end.appendleft(end[0])
            
            sl.add((cp[i][1], i))
            if len(sl) > 1:
                secondEnd.appendleft(sl[1][0])
            else:
                secondEnd.appendleft(n+1)
    
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
        
        ret = 0
        for i in range(m):
            ret = max(ret, cnt+better[i])
        
        return ret