# Last updated: 15/6/2025, 9:38:58 am
class Solution:
    def numberOfComponents(self, prop: List[List[int]], k: int) -> int:
        n = len(prop)
        m = len(prop[0])

        uniq = []

        for i in range(n):
            u = {}
            for j in range(m):
                u[prop[i][j]] = 1
            uniq.append(u)
        
        parents = [i for i in range(n)]
        sizes = [1] * n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            x = find(x)
            y = find(y)

            if x == y: return True

            if sizes[y] > sizes[x]:
                x, y = y, x
            
            sizes[x] += sizes[y]
            parents[y] = x
            
            return False

        for i in range(n):
            for j in range(i+1, n):
                cnt = 0
                for num in uniq[j]:
                    if num in uniq[i]: cnt += 1
                
                if cnt >= k: union(i, j)
        
        ret = 0
        for i, node in enumerate(parents):
            if node == i: ret += 1
        
        return ret
                        