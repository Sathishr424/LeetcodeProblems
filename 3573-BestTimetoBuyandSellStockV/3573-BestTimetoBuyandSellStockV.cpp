// Last updated: 12/18/2025, 1:19:17 PM
1const int N = 1e5 + 1;
2const long inf = LONG_MAX;
3long long dp[N][2];
4
5class Solution {
6public:
7    long long rec(int index, int done, vector<long long>& prefix, vector<int>& prices, vector<int>& strategy, int k, int n) {
8        if (dp[index][done] != inf) return dp[index][done];
9        if (index == n) {
10            return 0;
11        }
12
13        long long ans = rec(index + 1, done, prefix, prices, strategy, k, n) + (strategy[index] * prices[index]);
14        if (done == 0 && index + k <= n) {
15            ans = max(ans, rec(index + k, 1, prefix, prices, strategy, k, n) + (prefix[index + k] - prefix[index + (k / 2)]));
16        }
17
18        dp[index][done] = ans;
19        return ans;
20    }
21
22    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
23        int n = prices.size();
24        vector<long long> prefix(n+1, 0);
25        for (int i=0; i<n; i++) {
26            prefix[i + 1] = prefix[i] + prices[i];
27        }
28        fill(&dp[0][0], &dp[0][0] + 0LL + N * 2, inf);
29
30        return rec(0, 0, prefix, prices, strategy, k, n);
31    }
32};