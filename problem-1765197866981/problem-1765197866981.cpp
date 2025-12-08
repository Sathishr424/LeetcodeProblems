// Last updated: 12/8/2025, 6:14:26 PM
1struct Vec2 {
2    int num;
3    int index;
4};
5
6class Solution {
7public:
8    long long findScore(vector<int>& nums) {
9        int n = nums.size();
10        vector<Vec2> arr;
11
12        long long score = 0;
13        for (int i=0; i<n; i++) {
14            arr.push_back({nums[i], i});
15        }
16
17        sort(arr.begin(), arr.end(), [](auto &a, auto &b) {
18            return a.num < b.num || (a.num == b.num && a.index < b.index);
19        });
20
21        vector<int> marked(n, 0);
22        for (auto t: arr) {
23            if (marked[t.index]) continue;
24            marked[t.index] = 1;
25            if (t.index > 0) marked[t.index - 1] = 1;
26            if (t.index + 1 < n) marked[t.index + 1] = 1;
27            score += t.num;
28        }
29
30        return score;
31    }
32};