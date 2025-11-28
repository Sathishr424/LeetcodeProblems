// Last updated: 28/11/2025, 5:50:28 pm
1class Solution {
2public:
3    int dfs(int x, int parent, vector<vector<int>>& graph, vector<int>& values, vector<int>& sums, int k) {
4        int sum = values[x];
5        for (int y: graph[x]) {
6            if (y == parent) continue;
7            sum += dfs(y, x, graph, values, sums, k);
8            sum %= k;
9        }
10        sums[x] = sum;
11        return sum;
12    }
13
14    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
15        vector<vector<int>> graph(n, vector<int>());
16        for (auto edge : edges) {
17            graph[edge[0]].push_back(edge[1]);
18            graph[edge[1]].push_back(edge[0]);
19        }
20
21        vector<int> sums(n);
22        dfs(0, -1, graph, values, sums, k);
23
24        int ans = 0;
25        for (int i = 0; i < sums.size(); i++) {
26            if (sums[i] % k == 0) {
27                ans++;
28            }
29        }
30
31        return ans;
32    }
33};
34