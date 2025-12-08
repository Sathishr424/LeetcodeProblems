// Last updated: 12/8/2025, 8:15:27 AM
1class Solution {
2public:
3    int countTriples(int n) {
4        long long count = 0;
5        for (int i=1; i<=n; i++) {
6            for (int j=1; j<=n; j++) {
7                for (int k=1; k<=n; k++) {
8                    if (i == j || i == k || j == k) continue;
9                    if (i*i + j*j == k*k) count++;
10                }
11            }
12        }
13        return count;
14    }
15};