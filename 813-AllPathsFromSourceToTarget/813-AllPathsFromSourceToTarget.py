# Last updated: 12/6/2025, 5:46:33 am
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ret = []
        def dfs(x, arr):
            arr.append(x)
            if x == len(graph)-1: 
                ret.append(arr + [])
            else:
                for y in graph[x]:
                    dfs(y, arr)
            arr.pop()
        dfs(0, [])
        return ret