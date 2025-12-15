// Last updated: 12/15/2025, 12:19:57 PM
1class Solution {
2public:
3    long long getDescentPeriods(vector<int>& prices) {
4        int n = prices.size();
5        int cnt = 0;
6
7        int prev = prices[0] + 1;
8        long long ans = 0;
9        for (int i=0; i<n; i++) {
10            if (prev - prices[i] == 1) {
11                cnt++;
12            } else {
13                cnt = 1;
14            }
15            ans += cnt;
16            prev = prices[i];
17        }
18
19        return ans;
20    }
21};