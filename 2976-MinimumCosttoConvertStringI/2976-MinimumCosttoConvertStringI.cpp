// Last updated: 1/29/2026, 7:29:28 PM
1#include <climits>
2#include <deque>
3#include <iostream>
4#include <vector>
5
6using namespace std;
7
8class Solution {
9public:
10  long long minimumCost(string source, string target, vector<char> &original,
11                        vector<char> &changed, vector<int> &cost) {
12    int n = source.length();
13    int m = original.size();
14
15    vector<vector<pair<int, int>>> graph(26);
16
17    for (int i = 0; i < m; i++) {
18      graph[original[i] - 'a'].push_back({changed[i] - 'a', cost[i]});
19    }
20
21    vector<vector<int>> best(26, vector<int>(26, INT_MAX));
22    vector<tuple<int, int, int>> stack;
23    for (int i = 0; i < 26; i++) {
24      stack.push_back(make_tuple(i, i, 0));
25      best[i][i] = 0;
26    }
27
28    while (stack.size()) {
29      auto [t, a, c] = stack.back();
30      stack.pop_back();
31
32      for (auto &row : graph[a]) {
33        int new_cost = c + row.second;
34        if (new_cost < best[t][row.first]) {
35          stack.push_back({t, row.first, new_cost});
36          best[t][row.first] = new_cost;
37        }
38      }
39    }
40
41    long long ans = 0;
42    for (int i = 0; i < n; i++) {
43      int a = source[i] - 'a';
44      int b = target[i] - 'a';
45
46      if (best[a][b] == INT_MAX)
47        return -1;
48      ans += best[a][b];
49    }
50
51    return ans;
52  }
53};
54