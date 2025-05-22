# Last updated: 22/5/2025, 5:49:55 pm
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        q = deque(sorted(queries))
        h = []
        
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
            
            while q and q[0][0] <= index:
                curr = q.popleft()
                if curr[1] >= index:
                    heapq.heappush(h, -curr[1])
                else:
                    extra += 1

            while h and need:
                y = heapq.heappop(h)
                if -y < index:
                    extra += 1
                    continue
                
                lines[(-y) + 1] -= 1
                prefix += 1
                need -= 1
            
            if need > 0: return -1
            
        return extra + len(q) + len(h)