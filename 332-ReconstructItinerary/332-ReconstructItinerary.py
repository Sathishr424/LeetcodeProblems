# Last updated: 13/8/2025, 5:07:42 pm
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for f, t in tickets:
            graph[f].append(t)
        
        for f in graph:
            graph[f].sort(reverse=True)
        
        ret = []
        
        def dfs(x):
            while graph[x]:
                dfs(graph[x].pop())
            
            ret.append(x)
        
        dfs('JFK')
        return ret[::-1]

