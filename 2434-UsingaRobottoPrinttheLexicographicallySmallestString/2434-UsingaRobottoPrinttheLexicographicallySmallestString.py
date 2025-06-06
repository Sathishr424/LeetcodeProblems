# Last updated: 6/6/2025, 12:49:46 pm
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        ret = []
        
        heap = []
        for i in range(n):
            heap.append((s[i], i))
        heapq.heapify(heap)

        t = []
        index = 0

        while index < n:
            while heap[0][1] < index:
                heapq.heappop(heap)
            if not t or heap[0][0] < t[-1]:
                curr, i = heapq.heappop(heap)
                ret.append(curr)
                for j in range(index, i):
                    t.append(s[j])
                index = i+1
            else:
                ret.append(t.pop())
        
        while t:
            ret.append(t.pop())

        return ''.join(ret)