# Last updated: 12/6/2025, 5:39:03 am
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # TODO
        graph = [set() for _ in range(n + 1)]
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        
        curr = {1, }
        visited = set()
        answer = None
        l = 0
        while not answer: 
            nxt = set()
            for x in curr:  
                if x == n:
                    answer = l
                nxt |= graph[x] 
            nxt -= visited 

            visited |= curr
            curr = nxt 
            l += 1
        
        if n in curr:
            answer += 1
        else:
            answer += 2
        
        ttl = 0
        while answer:
            phase = ttl % (change * 2)
            if phase >= change:
                ttl += (2 * change - phase)
            ttl += time
            answer -= 1
        return ttl