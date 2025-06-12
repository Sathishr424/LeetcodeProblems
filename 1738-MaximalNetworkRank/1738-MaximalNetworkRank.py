# Last updated: 12/6/2025, 5:40:44 am
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(lambda: {})
        for road in roads:
            graph[road[0]][road[1]] = 1
            graph[road[1]][road[0]] = 1

        ret = 0
        for i in range(n-1):
            for j in range(i+1,n):
                cnt = len(graph[i]) + len(graph[j])
                if i in graph[j]: cnt -= 1
                ret = max(ret, cnt)

        return ret