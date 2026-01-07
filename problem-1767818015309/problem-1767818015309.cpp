// Last updated: 1/8/2026, 2:03:35 AM
1
2class Solution {
3public:
4  int maximumCostSubstring(string s, string chars, vector<int> &vals) {
5    int alp[26];
6
7    for (int i = 0; i < 26; i++)
8      alp[i] = i + 1;
9
10    for (int i = 0; i < chars.length(); i++) {
11      char c = chars[i];
12      alp[c - 'a'] = vals[i];
13    }
14
15    int best = 0;
16    int curr = 0;
17
18    for (char c : s) {
19      curr = max(curr + alp[c - 'a'], alp[c - 'a']);
20      best = max(best, curr);
21    }
22    return best;
23  }
24};
25