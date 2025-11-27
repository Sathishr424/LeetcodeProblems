// Last updated: 27/11/2025, 9:31:16 am
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
12            curr = ((curr + nums[i]) % k + k) % k;
13            ans+=last_seen[curr];
14            last_seen[curr]++;
15        }
16
17        return ans;
18    }
19};