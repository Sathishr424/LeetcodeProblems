// Last updated: 12/11/2025, 7:31:37 PM
1class Solution {
2public:
3    vector<int> maxSubgraphScore(int n, vector<vector<int>>& edges, vector<int>& good) {
4        unordered_map<int, vector<int>> graph;
5        for (int i=0; i<n; i++) {
6            good[i] = good[i] == 0 ? -1 : 1;
7        }
8
9        vector<int> costs(n, 0);
10
11        for (auto& edge: edges) {
12            graph[edge[0]].push_back(edge[1]);
13            graph[edge[1]].push_back(edge[0]);
14        }
15
16        function<int(int,int)> dfs = [&](int x, int par) -> int {
17            int total_cost = good[x];
18            for (int y: graph[x]) {
19                if (y == par) continue;
20                int cost = dfs(y, x);
21                total_cost += max(0, cost);
22            }
23            costs[x] = total_cost;
24            return total_cost;
25        };
26
27        dfs(0, -1);
28        vector<int> ret(n, 0);
29
30        function<void(int,int,int)> dfs2 = [&](int x, int par, int cost_so_far) {
31            int cost = costs[x];
32            
33            if (cost <= 0) {
34                cost_so_far += cost;
35                ret[x] = max(cost, cost_so_far);
36            } else {
37                ret[x] = max(cost, cost_so_far);
38            }
39
40            for (int y: graph[x]) {
41                if (y == par) continue;
42                dfs2(y, x, max(cost_so_far, cost));
43            }
44        };
45        
46        dfs2(0, -1, costs[0]);
47        return ret;
48    }
49};