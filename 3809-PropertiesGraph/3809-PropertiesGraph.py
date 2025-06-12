# Last updated: 12/6/2025, 5:34:03 am
class Solution:
    def numberOfComponents(self, prop: List[List[int]], diff: int) -> int:
        n = len(prop)
        m = len(prop[0])

        parents = [i for i in range(n)]
        sizes = [1] * n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            node1 = find(x)
            node2 = find(y)

            if node1 == node2: return 1

            if sizes[node2] > sizes[node1]:
                node1, node2 = node2, node1
            
            parents[node2] = node1
            sizes[node1] += sizes[node2]

        counts = defaultdict(dict)

        for i in range(n):
            for j in range(m):
                counts[prop[i][j]][i] = 1
        # print(dict(counts))
        for i in range(n):
            curr = defaultdict(int)
            vis = {}

            for j in range(m):
                x = prop[i][j]
                if x in vis: continue
                for y in counts[x]:
                    curr[y] += 1
                vis[x] = 1

            # print(i, curr)
            for y in curr:
                if curr[y] >= diff:
                    # print(i, y)
                    union(i, y)
        # print(parents)
        ret = 0
        for i in range(n):
            if find(i) == i: 
                ret += 1
        
        return ret