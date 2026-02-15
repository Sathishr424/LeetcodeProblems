// Last updated: 2/15/2026, 7:24:38 PM
1#include <iostream>
2#include <vector>
3#include <cstring>
4
5using namespace std;
6
7class Solution {
8public:
9  vector<int> toggleLightBulbs(vector<int> &bulbs) {
10    int on[101];
11    memset(on, 0, sizeof(on));
12
13    for (int& b: bulbs) {
14      on[b] = on[b] == 1 ? 0 : 1;
15    }
16
17    vector<int> ret;
18    for (int i=0; i<=100; i++) {
19      if (on[i] == 1) ret.push_back(i);
20    }
21
22    return ret;
23  }
24};
25