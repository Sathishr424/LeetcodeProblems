// Last updated: 12/9/2025, 4:27:32 AM
1class Solution {
2public:
3    vector<int> evenOddBit(int n) {
4        int index = 0;
5        int odd = 0;
6        int even = 0;
7        while (n) {
8            if (n & 1) {
9                if (index % 2 == 0) even++;
10                else odd++;
11            }
12            index++;
13            n >>= 1;
14        }
15
16        return {even, odd};
17    }
18};