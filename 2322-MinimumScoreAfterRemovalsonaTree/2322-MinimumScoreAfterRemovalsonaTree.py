# Last updated: 24/7/2025, 1:30:37 pm
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums) + 1

        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        xors = [0] * n
        edge_scores = {}
        node_childs = [{} for _ in range(n)]

        def dfs(x, par):
            curr = 0
            childs = {}
            childs[x] = 1
            for y in graph[x]:
                if y == par: continue
                s, c = dfs(y, x)
                for node in c:
                    childs[node] = 1
                edge_scores[(x, y)] = s
                curr ^= s
            node_childs[x] = childs
            xors[x] = curr ^ nums[x]
            return xors[x], childs
        
        s, c = dfs(0, -1)
        c[0] = 1
        node_childs[0] = c
        # print(xors)
        # print(node_childs)
        ret = inf
        m = len(edges)
        for i in range(m):
            main_score = xors[0]
            x, y = edges[i]
            if (x, y) not in edge_scores:
                x, y = y, x
            main_score ^= xors[y]
            second_score = xors[y]
            # print((x,y), main_score, second_score)
            for j in range(i+1, m):
                x2, y2 = edges[j]
                if (x2, y2) not in edge_scores:
                    x2, y2 = y2, x2

                new_main_score = main_score
                new_second_score = second_score
                third_score = xors[y2]

                # print((x2, y2), xors[y2])
                if y2 in node_childs[y]:
                    # print('second to third', new_second_score, '^', third_score, '=', new_second_score ^ third_score)
                    new_second_score ^= third_score
                elif y in node_childs[y2]:
                    # print('first to third', new_main_score, '^', third_score, '=', new_main_score ^ third_score)
                    new_main_score = xors[0] ^ third_score
                    third_score ^= second_score
                else:
                    new_main_score ^= third_score
                
                # print(new_main_score, new_second_score, third_score)
                maxi = max(new_main_score, new_second_score, third_score)
                mini = min(new_main_score, new_second_score, third_score)

                ret = min(ret, maxi - mini)
            # print()
        
        return ret
