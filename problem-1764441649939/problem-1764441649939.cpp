// Last updated: 30/11/2025, 12:10:49 am
1class Solution {
2public:
3    int maxScore(vector<int>& nums) {
4        sort(nums.begin(), nums.end(), [](int a, int b) {return a > b;});
5        long long p = 0;
6        int cnt = 0;
7        for (int num: nums) {
8            p+=num;
9            if (p <= 0) break;
10            cnt++;
11        }
12        return cnt;
13    }
14};