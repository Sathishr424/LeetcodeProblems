# Last updated: 7/6/2025, 2:45:41 am
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
        end.append(m-1)
        secondEnd = deque([])
        secondEnd.append(n+1)

        sl = SortedList()
        sl.add(cp[-1][1])

        for i in range(len(cp)-2, -1, -1):
            if cp[i][1] < cp[end[0]][1]:
                end.appendleft(i)
            else:
                end.appendleft(end[0])
            
            sl.add(cp[i][1])
            if len(sl) > 1:
                secondEnd.appendleft(sl[1])
                if len(sl) > 2: sl.pop()
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
        
        return cnt + max(better)