# Last updated: 12/6/2025, 5:41:00 am
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for x, y in edges: graph[y] = 1
        ret = []
        for i in range(n):
            if i not in graph:
                ret.append(i)
        return ret