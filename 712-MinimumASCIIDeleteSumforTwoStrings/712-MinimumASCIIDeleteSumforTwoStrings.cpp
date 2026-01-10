// Last updated: 1/10/2026, 3:55:57 PM
1
2int dp[1001][1001];
3int inf = 1e9 * 2;
4
5int rec(int i, int j, int &m, int &n, string &s1, string &s2,
6        vector<int> &prefix_1, vector<int> &prefix_2) {
7  if (dp[i][j] != -1)
8    return dp[i][j];
9
10  if (i == m)
11    return prefix_2[n] - prefix_2[j];
12  if (j == n)
13    return prefix_1[m] - prefix_1[i];
14
15  int ans = min(rec(i + 1, j, m, n, s1, s2, prefix_1, prefix_2) + s1[i],
16                rec(i, j + 1, m, n, s1, s2, prefix_1, prefix_2) + s2[j]);
17  if (s1[i] == s2[j])
18    ans = min(ans, rec(i + 1, j + 1, m, n, s1, s2, prefix_1, prefix_2));
19
20  dp[i][j] = ans;
21  return ans;
22}
23
24class Solution {
25public:
26  int minimumDeleteSum(string s1, string s2) {
27    memset(dp, -1, sizeof(dp));
28    int m = s1.length();
29    int n = s2.length();
30
31    vector<int> prefix_1(m + 1, 0), prefix_2(n + 1, 0);
32    int val = 0;
33    for (int i = 0; i < m; i++) {
34      prefix_1[i] = val;
35      val += s1[i];
36    }
37    prefix_1[m] = val;
38
39    val = 0;
40    for (int i = 0; i < n; i++) {
41      prefix_2[i] = val;
42      val += s2[i];
43    }
44    prefix_2[n] = val;
45
46    return rec(0, 0, m, n, s1, s2, prefix_1, prefix_2);
47  }
48};
49