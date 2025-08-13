# Last updated: 13/8/2025, 6:12:57 pm
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        n = len(pairs)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        graph = defaultdict(list)
        there = {}
        for x, y in pairs:
            graph[x].append(y)
            there[x] = 1
            there[y] = 1
            in_degree[y] += 1
            out_degree[x] += 1
        
        s = pairs[0][1]
        for x in there:
            if out_degree[x] > in_degree[x]:
                s = x
                break

        ret = []
        def dfs_el(x, par):
            while graph[x]:
                dfs_el(graph[x].pop(), x)
            
            ret.append([par, x])
        
        dfs_el(s, -1)

        return ret[::-1][1:]