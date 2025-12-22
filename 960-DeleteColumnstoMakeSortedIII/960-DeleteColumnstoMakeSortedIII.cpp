// Last updated: 22/12/2025, 3:59:28 pm
1int dp[101][101][102];
2
3class Solution {
4public:
5    bool isCurrentIndexLargerThanPrev(int index, int prev_index, vector<string>& strs, int& n) {
6        for (int i=0; i<n; i++) {
7            if (strs[i][index] < strs[i][prev_index]) return false;
8        }
9        return true;
10    }
11
12    int rec(int index, int prev_index, int prev_prev_index, vector<string>& strs, int& n, int& m) {
13        if (dp[index][prev_index][prev_prev_index] != -1) return dp[index][prev_index][prev_prev_index];
14        if (index == m) return 0;
15
16        int ans = rec(index + 1, prev_index, prev_prev_index, strs, n, m) + 1;
17        if (isCurrentIndexLargerThanPrev(index, prev_index, strs, n)) {
18            ans = min(ans, rec(index + 1, index, prev_index, strs, n, m));
19        } else if (prev_prev_index == 101 || isCurrentIndexLargerThanPrev(index, prev_prev_index, strs, n)) {
20            ans = min(ans, rec(index + 1, index, prev_prev_index, strs, n, m) + 1);
21        }
22        dp[index][prev_index][prev_prev_index] = ans;
23        return ans;
24    }
25
26    int minDeletionSize(vector<string>& strs) {
27        int n = strs.size();
28        int m = strs[0].length();
29        memset(dp, -1, sizeof(dp));
30        return rec(1, 0, 101, strs, n, m);
31    }
32};