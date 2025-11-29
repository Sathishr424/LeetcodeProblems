// Last updated: 29/11/2025, 7:18:05 am
1class Solution {
2public:
3    int minOperations(vector<int>& nums, int k) {
4        int total = 0;
5        for (int num: nums) {
6            total += num;
7        }
8
9        return total % k;
10    }
11};