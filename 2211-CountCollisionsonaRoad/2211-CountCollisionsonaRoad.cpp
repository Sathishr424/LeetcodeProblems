// Last updated: 4/12/2025, 8:27:16 am
1class Solution {
2public:
3    int countCollisions(string directions) {
4        int right = 0;
5        bool isLastStationary = false;
6        int collisions = 0;
7        for (char c: directions) {
8            if (c == 'L') {
9                if (isLastStationary) collisions++;
10                else if (right) {
11                    collisions += right + 1;
12                    isLastStationary = true;
13                    right = 0;
14                }
15            } else if (c == 'R') {
16                isLastStationary = false;
17                right++;
18            } else {
19                collisions += right;
20                isLastStationary = true;
21                right = 0;
22            }
23        }
24        return collisions;
25    }
26};