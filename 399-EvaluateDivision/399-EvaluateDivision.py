# Last updated: 12/6/2025, 5:49:53 am
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hash = defaultdict(dict)

        for i, (x, y) in enumerate(equations):
            hash[x][y] = values[i]
            hash[y][x] = 1/values[i]
        
        def dfs(x, y, val, vis={}):
            # print(x, y, val)
            if x == y: return val
            for z in hash[x]:
                if z not in vis:
                    vis[z] = 1
                    ans = dfs(z, y, val*hash[x][z], vis)
                    if ans != float('inf'): return ans
            return float('inf')
        # print(dict(hash))
        ret = []
        for x, y in queries:
            if x not in hash or y not in hash: 
                ret.append(-1)
                continue
            ans = dfs(x, y, 1, {x: 1})
            if ans == float('inf'): ret.append(-1)
            else: ret.append(ans)
        
        return ret
            