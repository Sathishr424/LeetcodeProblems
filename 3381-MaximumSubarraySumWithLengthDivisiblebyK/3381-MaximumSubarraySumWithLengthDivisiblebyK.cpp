// Last updated: 28/11/2025, 12:00:43 am
1class Solution {
2public:
3    long long maxSubarraySum(vector<int>& nums, int k) {
4        int n = nums.size();
5        unordered_map<int, long long> seen;
6
7        long long best_sum = LLONG_MIN;
8        long long sum = 0;
9        seen[0] = 0;
10        for (int i=0; i<n; i++) {
11            sum += nums[i];
12            int rem = (i + 1) % k;
13            if (seen.find(rem) != seen.end()) {
14                best_sum = max(best_sum, sum - seen[rem]);
15                seen[rem] = min(seen[rem], sum);
16            } else {
17                seen[rem] = sum;
18            }
19        }
20
21        return best_sum;
22    }
23};