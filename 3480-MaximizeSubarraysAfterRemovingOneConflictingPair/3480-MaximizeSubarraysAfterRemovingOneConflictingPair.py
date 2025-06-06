# Last updated: 7/6/2025, 2:28:11 am
class Solution:
    def maxSubarrays(self, n: int, cp: List[List[int]]) -> int:
        m = len(cp)
        new_cp = []
        for x, y in cp:
            new_cp.append([min(x,y), max(x,y)])
        cp = new_cp
        cp.sort()
        # print(cp)
        better = [0] * m

        def calcScore(cp):
            m = len(cp)
            if m == 0: return n*(n+1)//2
            start = []
            end = []

            for x,y in cp:
                start.append(x)
            
            end = deque([])
            end.append(m-1)
            secondEnd = deque([])
            secondEnd.append(m)

            heap = SortedList()
            heap.add((cp[-1][1], m-1))

            for i in range(len(cp)-2, -1, -1):
                if cp[i][1] < cp[end[0]][1]:
                    end.appendleft(i)
                else:
                    end.appendleft(end[0])
                
                heap.add((cp[i][1], i))
                if len(heap) > 1:
                    secondEnd.appendleft(heap[1][1])
                else:
                    secondEnd.appendleft(m)

            # print(end)
            # print(secondEnd)
            cnt = 0
            for i in range(n, 0, -1):
                index = bisect_left(start, i)
                if index < m:
                    index_2 = end[index]
                    diff = cp[index_2][1] - i
                    cnt += diff
                    index_3 = m
                    if secondEnd[index] < m:
                        index_3 = secondEnd[index]
                        better[index_2] += (cp[index_3][1] - i) - diff
                    else:
                        better[index_2] += (n - i + 1) - diff

                    # print(i, index, cp[index_2], cp[index_3] if index_3 < m else '-', diff)
                else:
                    # print(i, n-i+1)
                    cnt += n-i+1
            # print(cnt)
            return cnt
        
        cnt = calcScore(cp)
        # print(cnt, better)

        # maxi = 0
        ret = 0
        for i in range(m):
            ret = max(ret, cnt+better[i])
        return ret
        
        # cp = cp[:maxi] + cp[maxi+1:]

        # return calcScore(cp)