# Last updated: 6/6/2025, 12:43:47 pm
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        ret = ''
        
        heap = []

        for i in range(n):
            heapq.heappush(heap, (s[i], i))

        t = []
        index = 0

        while index < n:
            while heap[0][1] < index:
                heapq.heappop(heap)
            if not t or heap[0][0] < t[-1]:
                curr, i = heapq.heappop(heap)
                ret += curr
                for j in range(index, i):
                    t.append(s[j])
                index = i+1
            else:
                ret += t.pop()
        
        while t:
            ret += t.pop()

        return ret