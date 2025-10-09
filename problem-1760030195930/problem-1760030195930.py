# Last updated: 9/10/2025, 10:46:35 pm
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = defaultdict(list)
        costs = defaultdict(list)
        costs_dict = defaultdict(dict)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        max_possible_cost = 0
        def dfs(x, par, cost):
            nonlocal max_possible_cost
            cost += price[x]
            max_cost = cost
            for y in graph[x]:
                if y == par: continue
                c = dfs(y, x, cost)
                max_cost = max(c, max_cost)
                costs[x].append(c - cost + price[x])
                costs_dict[x][y] = c - cost + price[x]
            costs[x].sort(key=lambda z: -z)
            
            return max_cost

        dfs(0, -1, 0)

        sl = SortedList([0])
        def dfs3(x, par, cost):
            nonlocal max_possible_cost
            # print(x, cost, sl)
            c = costs[x]
            sub = 0
            if c:
                sub += c[0]
                max_possible_cost = max(max_possible_cost, sub - price[x])
            if sl:
                # print(sub, sl[-1], price[x])
                max_possible_cost = max(max_possible_cost, sl[-1] + cost)
            
            cost += price[x]
            for y in graph[x]:
                if y == par: continue
                added = inf
                if costs_dict[x][y] == c[0]:
                    if len(c) > 1:
                        added = c[1]
                        sl.add(c[1] - cost)
                else:
                    added = c[0]
                    sl.add(c[0] - cost)
                dfs3(y, x, cost)
                if added != inf:
                    sl.remove(added - cost)

        dfs3(0, -1, 0)
        return max_possible_cost