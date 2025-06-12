# Last updated: 12/6/2025, 5:41:28 am
class Solution:
    def minReorder(self, n: int, conn: List[List[int]]) -> int:
        graph = defaultdict(list)
        alter = defaultdict(list)

        res = 0
        for x, y in conn:
            graph[x].append(y)
            alter[y].append(x)
        
        stack = [0]
        vis = {0: 1}
 
        while stack:
            node = stack.pop()
            for x in graph[node]:
                if x not in vis: 
                    stack.append(x)
                    vis[x] = 1
                    res += 1
            
            for x in alter[node]:
                if x not in vis: 
                    stack.append(x)
                    vis[x] = 1

        return res
