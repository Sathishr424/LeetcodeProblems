# Last updated: 7/6/2025, 4:19:41 pm
class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)

        deleted = [0] * n
        heap = []
        for i in range(n):
            if s[i] == '*':
                deleted[i] = 1
                deleted[-heapq.heappop(heap)[1]] = 1
            else:
                heapq.heappush(heap, (s[i], -i))
        
        ret = []    

        for i in range(n):
            if deleted[i] == 0:
                ret.append(s[i])
        
        return ''.join(ret)
                
