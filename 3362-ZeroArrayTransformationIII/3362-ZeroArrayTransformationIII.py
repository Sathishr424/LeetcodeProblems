# Last updated: 22/5/2025, 4:53:34 pm
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        q = deque(sorted(queries))
        
        lines = [0] * (n+1)
        prefix = 0
        extra = 0

        for index, num in enumerate(nums):
            prefix += lines[index]
            need = num - prefix

            if need <= 0: continue

            while q and q[0][1] < index:
                q.popleft()
                extra += 1
            
            h = []
            while q and q[0][0] <= index:
                curr = q.popleft()
                if curr[1] >= index:
                    heapq.heappush(h, (-curr[1], curr[0]))
                else:
                    extra += 1

            if len(h) < need: return -1

            while need:
                y, x = heapq.heappop(h)

                lines[(-y) + 1] -= 1
                prefix += 1
                need -= 1
            
            for y, x in sorted(h, key=lambda x: x[1]):
                q.appendleft([x, -y])
            
        return extra + len(q)