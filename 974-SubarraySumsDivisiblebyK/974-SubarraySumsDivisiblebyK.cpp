// Last updated: 27/11/2025, 9:27:20 am
1class Solution {
2public:
3    int subarraysDivByK(vector<int>& nums, int k) {
4        int n = nums.size();
5
6        unordered_map<int, int> last_seen;
7
8        int ans = 0;
9        int curr = 0;
10        last_seen[curr]++;
11        for (int i=0; i<n; i++) {
12            curr = (curr + nums[i]) % k;
13            int rem = (curr + k) % k;
14            if (last_seen.find(rem) != last_seen.end()) {
15                ans+=last_seen[rem];
16            }
17            last_seen[rem]++;
18            // cout << i << " " << rem << ", " << ans << endl;
19        }
20
21        return ans;
22    }
23};