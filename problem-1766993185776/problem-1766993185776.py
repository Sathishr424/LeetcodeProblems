# Last updated: 12/29/2025, 12:56:25 PM
1class Solution:
2    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
3        start = len(bottom)
4        there = defaultdict(list)
5        for st in allowed:
6            there[st[:2]].append(st[2])
7        
8        def dfs(prev, index, row, curr):
9            if row == 0: return True
10            if index == row: return dfs(curr, 0, row - 1, '')
11            c = prev[index] + prev[index + 1]
12            
13            for top in there[c]:
14                if dfs(prev, index + 1, row, curr + top): return True
15            
16            return False
17
18        return dfs(bottom, 0, start - 1, '')