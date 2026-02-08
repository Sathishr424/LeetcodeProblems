// Last updated: 2/8/2026, 4:14:03 PM
1class Solution {
2public:
3    bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
4        int diff = max(abs(sx - fx),  abs(sy - fy));
5        if (diff == 0 && t == 1) return false;
6
7        if (diff <= t) return true;
8        return false;
9    }
10};