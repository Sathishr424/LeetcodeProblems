# Last updated: 22/5/2025, 5:48:20 pm
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        q = deque(sorted(queries))
        m = len(q)
        h = []
        
        lines = [0] * (n+1)
        prefix = 0
        extra = 0
        left = 0

        for index, num in enumerate(nums):
            prefix += lines[index]
            need = num - prefix

            if need <= 0: continue

            while left < m and q[left][1] < index:
                left += 1
                extra += 1
            
            while left < m and q[left][0] <= index:
                if q[left][1] >= index:
                    heapq.heappush(h, -q[left][1])
                else:
                    extra += 1
                left += 1

            while h and need:
                y = heapq.heappop(h)
                if -y < index:
                    extra += 1
                    continue
                
                lines[(-y) + 1] -= 1
                prefix += 1
                need -= 1
            
            if need > 0: return -1
            
        return extra + (m - left) + len(h)