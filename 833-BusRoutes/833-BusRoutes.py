# Last updated: 12/6/2025, 5:46:22 am
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source: return 0
        n = len(routes)
        arr = []
        indexes = []
        for i, r in enumerate(routes):
            arr.append({})
            indexes.append(i)
            for x in r:
                arr[-1][x] = 1
        
        stack = deque([])
        stack.append((target, 0))
        vis = {}
        vis[target] = 0

        while stack:
            route, bus = stack.popleft()
            newIndexes = []
            for i in indexes:
                if route in arr[i]:
                    for a in arr[i]:
                        if a not in vis:
                            if a == source: return bus+1
                            stack.append((a, bus+1))
                            vis[a] = 1
                else: newIndexes.append(i)
            indexes = newIndexes
        
        return -1