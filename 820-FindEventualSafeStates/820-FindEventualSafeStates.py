# Last updated: 12/6/2025, 5:46:28 am
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal = {}
        others = []
        ret = []
        n = len(graph)

        for i in range(n):
            if len(graph[i]) == 0:
                terminal[i] = 1
                ret.append(i)
            else: others.append(i)
        
        vis = {}

        def dfs(node, curr={}):
            if node in terminal: return True
            elif node in vis: return vis[node]
            curr[node] = 1

            for x in graph[node]:
                if x in curr or not dfs(x, curr):
                    vis[node] = False
                    return False
            del curr[node]
            vis[node] = True
            return True
        
        for node in others:
            x = {}
            if dfs(node, x):
                ret.append(node)
        
        return sorted(ret)