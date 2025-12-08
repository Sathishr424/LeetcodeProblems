// Last updated: 12/8/2025, 6:08:18 PM
1class Solution {
2public:
3    bool getPoss(vector<int>& nums, int mid, int n) {
4        int cnt = 0;
5        int left = 0;
6        int right = n - mid;
7        for (int i=right; i<right+n; i++) {
8            int index = i % n;
9            if (nums[index] > nums[left]) cnt++;
10            left++;
11        }
12        return cnt >= mid;
13    }
14    
15    int maximizeGreatness(vector<int>& nums) {
16        // 1, 1, 1, 2, 3, 3, 5
17        // 2, 3, 3, 5, 1, 1, 1
18        sort(nums.begin(), nums.end());
19        int n = nums.size();
20
21        int l = 0;
22        int r = n;
23
24        while (l < r) {
25            int mid = (l + r + 1) / 2;
26
27            if (getPoss(nums, mid, n)) {
28                l = mid;
29            } else {
30                r = mid - 1;
31            }
32        }
33
34        return l;
35    }
36};