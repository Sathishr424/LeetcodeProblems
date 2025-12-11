// Last updated: 12/11/2025, 7:35:30 PM
1class Solution {
2public:
3    int dfs(unordered_map<int, vector<int>>& graph, vector<int>& good, vector<int>& costs, int x, int par) {
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
14    void dfs2(unordered_map<int, vector<int>>& graph, vector<int>& costs, vector<int>& ret, int x, int par, int cost_so_far) {
15        int cost = costs[x];
16            
17        if (cost <= 0) {
18            cost_so_far += cost;
19            ret[x] = max(cost, cost_so_far);
20        } else {
21            ret[x] = max(cost, cost_so_far);
22        }
23
24        for (int y: graph[x]) {
25            if (y == par) continue;
26            dfs2(graph, costs, ret, y, x, max(cost_so_far, cost));
27        }
28    }
29
30    vector<int> maxSubgraphScore(int n, vector<vector<int>>& edges, vector<int>& good) {
31        vector<int> ret(n, 0);
32        vector<int> costs(n, 0);
33        unordered_map<int, vector<int>> graph;
34        for (int i=0; i<n; i++) {
35            good[i] = good[i] == 0 ? -1 : 1;
36        }
37
38        for (auto& edge: edges) {
39            graph[edge[0]].push_back(edge[1]);
40            graph[edge[1]].push_back(edge[0]);
41        }
42
43        dfs(graph, good, costs, 0, -1);
44        dfs2(graph, costs, ret, 0, -1, costs[0]);
45        
46        return ret;
47    }
48};