// Last updated: 12/8/2025, 5:52:44 PM
1class Solution {
2public:
3    int distMoney(int money, int children) {
4        for (int i=0; i<=children; i++) {
5            int rem = money - (8 * i);
6            int rem_c = children - i;
7            if (rem < rem_c) return i-1;
8            if (rem_c == 1 && rem == 4) return i-1;
9            if (rem_c == 0 && rem > 0) return i-1;
10        }
11        return children;
12    }
13};