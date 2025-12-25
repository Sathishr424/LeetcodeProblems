# Last updated: 12/25/2025, 7:12:02 PM
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

        m = max(nums) + 1
        childs = [0] * n
        cnts = [0] * m

        last = [-1] * m
        second_last = [-1] * m

        def dfs(x, par, start, two):
            nonlocal ret
            color = nums[x]

            if depths[last[color]] >= depths[start] and cnts[color] > 0:
                if two != -1:
                    index_1 = depths[second_last[two]]
                    index_2 = depths[last[color]]

                    if index_1 < index_2:
                        start = second_last[two]
                        two = color
                    else:
                        start = last[color]
                else:
                    two = color
            
            if start == -1:
                score = scores[x]
                nodes_cnt = depths[x] + 1
            else:
                prev_score = scores[start] + graph[start][childs[start]]
                score = scores[x] - prev_score
                nodes_cnt = depths[x] - depths[start]

            if score > ret[0]:
                ret = [score, nodes_cnt]
            elif score == ret[0] and nodes_cnt < ret[1]:
                ret[1] = nodes_cnt

            second_last_bu = second_last[color]
            last_bu = last[color]
            cnts[color] += 1

            second_last[color] = last[color]
            last[color] = x

            for y in graph[x]:
                if y == par: continue
                
                childs[x] = y
                dfs(y, x, start, two)

            second_last[color] = second_last_bu
            last[color] = last_bu
            cnts[color] -= 1
        
        dfs(0, -1, -1, -1)
        return ret