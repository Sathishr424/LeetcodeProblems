// Last updated: 12/25/2025, 7:11:06 PM
long long dp[1001][501][2][2];
int inf = INT_MAX;
const long long LINF = LONG_MAX;
class Solution {
public:
    long long rec(int index, int buying, int pending, vector<int>& prices, int rem, int n) {
        if (dp[index][rem][buying][pending] != inf) return dp[index][rem][buying][pending];
        if (index == n) {
            if (pending) return -inf;
            return 0;
        }
        if (rem == 0 && pending == 0) return 0;

        long long ans = rec(index + 1, buying, pending, prices, rem, n);
        if (pending == 0) {
            ans = max(ans, rec(index + 1, 0, 1, prices, rem - 1, n) - prices[index]);
            ans = max(ans, rec(index + 1, 1, 1, prices, rem - 1, n) + prices[index]);
        } else {
            if (buying) {
                ans = max(ans, rec(index + 1, buying ^ 1, 0, prices, rem, n) - prices[index]);
            } else {
                ans = max(ans, rec(index + 1, buying ^ 1, 0, prices, rem, n) + prices[index]);
            }
        }
        dp[index][rem][buying][pending] = ans;
        return ans;
    }

    long long maximumProfit(vector<int>& prices, int k) {
        fill(&dp[0][0][0][0],
          &dp[0][0][0][0] + 1001LL * 501 * 2 * 2,
          inf);

        return rec(0, 0, 0, prices, k, prices.size());
    }
};