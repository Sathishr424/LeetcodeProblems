# Last updated: 12/6/2025, 5:47:39 am
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        hash = defaultdict(int)
        for e in employees:
            hash[e.id] = e.importance
            for s in e.subordinates:
                graph[e.id].append(s)
        
        vis = {}
        def dfs(ID):
            imp = hash[ID]
            for e in graph[ID]:
                imp += dfs(e)
            return imp
        
        return dfs(id)
        