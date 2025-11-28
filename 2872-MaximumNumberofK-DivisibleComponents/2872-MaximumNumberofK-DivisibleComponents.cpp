// Last updated: 28/11/2025, 5:50:41 pm
1class Solution {
2public:
3    long long dfs(int x, int parent, vector<vector<int>>& graph, vector<int>& values, vector<long long>& sums) {
4        long long sum = values[x];
5        for (int y: graph[x]) {
6            if (y == parent) continue;
7            sum += dfs(y, x, graph, values, sums);
8        }
9        sums[x] = sum;
10        return sum;
11    }
12
13    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
14        vector<vector<int>> graph(n, vector<int>());
15        for (auto edge : edges) {
16            graph[edge[0]].push_back(edge[1]);
17            graph[edge[1]].push_back(edge[0]);
18        }
19
20        vector<long long> sums(n);
21        dfs(0, -1, graph, values, sums);
22
23        int ans = 0;
24        for (int i = 0; i < sums.size(); i++) {
25            if (sums[i] % k == 0) {
26                ans++;
27            }
28        }
29
30        return ans;
31    }
32};
33