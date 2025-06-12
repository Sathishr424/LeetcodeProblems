# Last updated: 13/6/2025, 4:51:36 am
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        ret = [0, 1]
        n = len(edges)+1
        graph = defaultdict(dict)

        for x, y, l in edges:
            graph[x][y] = l
            graph[y][x] = l
        
        depths = [0] * (n+1)
        scores = [0] * n

        def dfs_pre(x, par, depth, score):
            depths[x] = depth
            scores[x] = score
            for y in graph[x]:
                if y == par: continue

                dfs_pre(y, x, depth + 1, score + graph[x][y])
        
        dfs_pre(0, -1, 0, 0)

        def dfs(x, par, nodes, childs, last_cut):
            nonlocal ret
            prev = nodes[nums[x]]

            # print(x, last_cut, depths[x], scores[x])

            if depths[prev] >= depths[last_cut]:
                if cnts[nums[x]] == 0 and last_cut == n:
                    s = scores[x]
                    nodes_cnt = depths[x] + 1
                else:
                    prev_score = scores[prev] + graph[prev][childs[prev]]
                    s = scores[x] - prev_score
                    nodes_cnt = depths[x] - depths[prev]
                    last_cut = prev
                
                # print(x, (s, nodes_cnt))
            else:
                prev_score = scores[last_cut] + graph[last_cut][childs[last_cut]]

                s = scores[x] - prev_score
                nodes_cnt = depths[x] - depths[last_cut]

            # print(x, (s, nodes_cnt), 'no')
            
            if s > ret[0]:
                ret = [s, nodes_cnt]
            elif s == ret[0] and nodes_cnt < ret[1]:
                ret[1] = nodes_cnt

            nodes[nums[x]] = x
            cnts[nums[x]] += 1

            for y in graph[x]:
                if y == par: continue

                childs[x] = y
                dfs(y, x, nodes, childs, last_cut)
            
            nodes[nums[x]] = prev
            cnts[nums[x]] -= 1
        
        childs = defaultdict(int)
        cnts = defaultdict(int)

        dfs(0, -1, defaultdict(int), childs, n)

        return ret