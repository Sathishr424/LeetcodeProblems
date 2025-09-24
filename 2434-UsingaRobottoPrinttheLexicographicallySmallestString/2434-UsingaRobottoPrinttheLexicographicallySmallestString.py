# Last updated: 25/9/2025, 12:19:51 am
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)

        used = [0] * n

        heap = []
        for i, char in enumerate(s):
            heapq.heappush(heap, (char, i))

        t = []
        p = []
        right = 0
        while heap:
            if used[heap[0][1]]:
                heapq.heappop(heap)
                continue
            # print(heap, t, p)
            if t and t[-1] <= heap[0][0]:
                p.append(t.pop())
                continue
            
            char, index = heapq.heappop(heap)
            while right <= index:
                t.append(s[right])
                used[right] = 1
                right += 1
            p.append(t.pop())

        while t:
            p.append(t.pop())

        return ''.join(p)