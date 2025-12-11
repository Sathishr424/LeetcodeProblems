// Last updated: 12/11/2025, 7:47:54 PM
1class Solution {
2public:
3    int dfs(vector<vector<int>>& graph, vector<int>& good, vector<int>& costs, int x, int par) {
4        int total_cost = good[x];
5        for (int y: graph[x]) {
6            if (y == par) continue;
7            int cost = dfs(graph, good, costs, y, x);
8            total_cost += max(0, cost);
9        }
10        costs[x] = total_cost;
11        return total_cost;
12    }
13
14    void dfs2(vector<vector<int>>& graph, vector<int>& costs, vector<int>& ret, int x, int par, int cost_so_far) {
15        int cost = costs[x];
16            
17        if (cost <= 0) {
18            cost_so_far += cost;
19        }
20        ret[x] = max(cost, cost_so_far);
21
22        for (int y: graph[x]) {
23            if (y == par) continue;
24            dfs2(graph, costs, ret, y, x, max(cost_so_far, cost));
25        }
26    }
27
28    vector<int> maxSubgraphScore(int n, vector<vector<int>>& edges, vector<int>& good) {
29        vector<int> ret(n, 0);
30        vector<int> costs(n, 0);
31        vector<vector<int>> graph(n);
32        for (int i=0; i<n; i++) {
33            good[i] = good[i] == 0 ? -1 : 1;
34        }
35
36        for (auto& edge: edges) {
37            graph[edge[0]].push_back(edge[1]);
38            graph[edge[1]].push_back(edge[0]);
39        }
40
41        dfs(graph, good, costs, 0, -1);
42        dfs2(graph, costs, ret, 0, -1, costs[0]);
43
44        return ret;
45    }
46};