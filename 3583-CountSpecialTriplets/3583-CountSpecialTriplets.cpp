// Last updated: 12/9/2025, 6:22:30 AM
1const int N = 2e5 + 1;
2int left_freq[N];
3int right_freq[N];
4
5class Solution {
6public:
7    int specialTriplets(vector<int>& nums) {
8        int n = nums.size();
9        int mod = 1e9 + 7;
10
11        memset(left_freq, 0, sizeof(left_freq));
12        memset(right_freq, 0, sizeof(right_freq));
13
14        for (int num: nums) {
15            right_freq[num]++;
16        }
17
18        int ans = 0;
19        for (int num: nums) {
20            right_freq[num]--;
21
22            int need = num * 2;
23            ans += (left_freq[need] * 1LL * right_freq[need]) % mod;
24            ans %= mod;
25
26            left_freq[num]++;
27        }
28
29        return ans;
30    }
31};