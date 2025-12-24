// Last updated: 12/24/2025, 11:11:20 AM
1class Solution {
2public:
3    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
4        int total = accumulate(apple.begin(), apple.end(), 0);
5        sort(capacity.begin(), capacity.end());
6
7        int n = capacity.size();
8        for (int i=n-1; i>=0; i--) {
9            int can = min(total, capacity[i]);
10            total -= can;
11            if (total == 0) return n - i;
12        }
13
14        return n;
15    }
16};