# Last updated: 12/6/2025, 5:50:28 am
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        visited = {}
    
        graph = defaultdict(list)
        for x, y in tickets:
            graph[x].append(y)
        
        for x in graph: graph[x].sort(reverse=True)
        
        ret = []

        stack = ['JFK']

        while stack:
            x = stack[-1]
            
            if len(graph[x]) > 0:
                stack.append(graph[x].pop())
            else:
                ret.append(stack.pop())
        
        return ret[::-1]