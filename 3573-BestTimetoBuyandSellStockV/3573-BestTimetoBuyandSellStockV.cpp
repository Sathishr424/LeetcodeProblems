// Last updated: 12/18/2025, 1:38:37 PM
1class Solution {
2public:
3    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
4        int n = prices.size();
5        vector<long long> prefix(n+1, 0);
6        long long best = 0;
7        for (int i=0; i<n; i++) {
8            prefix[i + 1] = prefix[i] + prices[i];
9            best += prices[i] * strategy[i];
10        }
11
12        int half = k / 2;
13        long long left = 0;
14        long long right = 0;
15        for (int i=k; i<n; i++) {
16            right += (strategy[i] * prices[i]);
17        }
18
19        for (int i=0; i<n-k+1; i++) {
20            best = max(best, left + (prefix[i + k] - prefix[i + half]) + right);
21            left += (strategy[i] * prices[i]);
22            if (i + k < n)
23                right -= (strategy[i + k] * prices[i + k]);
24        }
25        
26        return best;
27    }
28};