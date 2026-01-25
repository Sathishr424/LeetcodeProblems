// Last updated: 1/25/2026, 2:19:14 PM
1#include <algorithm>
2#include <cmath>
3#include <iostream>
4#include <vector>
5using namespace std;
6
7class LCA {
8public:
9  vector<int> parents;
10  vector<int> dis;
11  vector<vector<int>> tree;
12  int m, n;
13
14  LCA(const vector<int> parents, const vector<int> dis) {
15    n = parents.size();
16    m = log2(n) + 1;
17    this->parents = parents;
18    this->dis = dis;
19    tree.resize(m, vector<int>(n, -1));
20    buildTree();
21  }
22
23  void buildTree() {
24    for (int i = 0; i < n; i++) {
25      tree[0][i] = parents[i];
26    }
27
28    for (int p = 1; p < m; p++) {
29      for (int i = 0; i < n; i++) {
30        if (tree[p - 1][i] == -1)
31          continue;
32
33        tree[p][i] = tree[p - 1][tree[p - 1][i]];
34      }
35    }
36  }
37
38  int up(int x, int d) {
39    for (int b = m - 1; b >= 0; b--) {
40      if ((1 << b) <= d && tree[b][x] != -1) {
41        x = tree[b][x];
42        d -= (1 << b);
43      }
44    }
45
46    return x;
47  }
48
49  int lca(int x, int y) {
50    if (x == y)
51      return x;
52
53    for (int i = m - 1; i >= 0; i--) {
54      if (tree[i][x] != -1 && tree[i][y] != -1 && tree[i][x] != tree[i][y]) {
55
56        x = tree[i][x];
57        y = tree[i][y];
58      }
59    }
60
61    return tree[0][x];
62  }
63
64  int findDis(int x, int y) {
65    int val = dis[x] + dis[y];
66    int d = abs(dis[x] - dis[y]);
67    if (dis[x] > dis[y]) {
68      x ^= y;
69      y ^= x;
70      x ^= y;
71    }
72
73    return val - dis[lca(x, up(y, d))] * 2;
74  }
75};
76
77void dfs(int x, int par, vector<vector<int>> &graph, vector<int> &parents,
78         vector<int> &dis, int level) {
79  parents[x] = par;
80  dis[x] = level;
81
82  for (int y : graph[x]) {
83    if (y == par)
84      continue;
85    dfs(y, x, graph, parents, dis, level + 1);
86  }
87}
88
89class Solution {
90public:
91  int specialNodes(int n, vector<vector<int>> &edges, int x, int y, int z) {
92    vector<int> parents(n, -1);
93    vector<int> dis(n);
94    vector<vector<int>> graph(n);
95
96    for (auto &edge : edges) {
97      graph[edge[0]].push_back(edge[1]);
98      graph[edge[1]].push_back(edge[0]);
99    }
100
101    dfs(0, -1, graph, parents, dis, 0);
102
103    LCA lca(parents, dis);
104    int ans = 0;
105
106    for (int i = 0; i < n; i++) {
107      vector<int> arr;
108      arr.push_back(lca.findDis(x, i));
109      arr.push_back(lca.findDis(y, i));
110      arr.push_back(lca.findDis(z, i));
111
112      sort(arr.begin(), arr.end());
113
114      int a = arr[0];
115      int b = arr[1];
116      int c = arr[2];
117
118      if ((a * 1LL * a) + 0LL + (b * 1LL * b) == c * 1LL * c)
119        ans++;
120    }
121
122    return ans;
123  }
124};
125