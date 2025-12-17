// Last updated: 12/17/2025, 1:09:50 PM
1long long dp[1001][501][2][2];
2int inf = INT_MAX;
3const long long LINF = LONG_MAX;
4class Solution {
5public:
6    long long rec(int index, int buying, int pending, vector<int>& prices, int rem, int n) {
7        if (dp[index][rem][buying][pending] != inf) return dp[index][rem][buying][pending];
8        if (index == n) {
9            if (pending) return -inf;
10            return 0;
11        }
12        if (rem == 0 && pending == 0) return 0;
13
14        long long ans = rec(index + 1, buying, pending, prices, rem, n);
15        if (pending == 0) {
16            ans = max(ans, rec(index + 1, 0, 1, prices, rem - 1, n) - prices[index]);
17            ans = max(ans, rec(index + 1, 1, 1, prices, rem - 1, n) + prices[index]);
18        } else {
19            if (buying) {
20                ans = max(ans, rec(index + 1, buying ^ 1, 0, prices, rem, n) - prices[index]);
21            } else {
22                ans = max(ans, rec(index + 1, buying ^ 1, 0, prices, rem, n) + prices[index]);
23            }
24        }
25        dp[index][rem][buying][pending] = ans;
26        return ans;
27    }
28
29    long long maximumProfit(vector<int>& prices, int k) {
30        fill(&dp[0][0][0][0],
31          &dp[0][0][0][0] + 1001LL * 501 * 2 * 2,
32          inf);
33
34        return rec(0, 0, 0, prices, k, prices.size());
35    }
36};