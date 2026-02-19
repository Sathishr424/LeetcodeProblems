// Last updated: 2/19/2026, 10:33:42 PM
1#include <iostream>
2#include <unordered_map>
3#include <cstring>
4#include <vector>
5const int N = 201;
6using namespace std;
7class Solution {
8public:
9  vector<vector<int>> findMatrix(vector<int> &nums) {
10    int n = nums.size();
11    int freq[N];
12    memset(freq, 0, sizeof(freq));
13
14    for (int& num: nums) freq[num]++;
15    vector<vector<int>> ret;
16
17    bool exist = true;
18    while (exist) {
19      vector<int> row;
20      exist = false;
21      for (int i=0; i<N; i++) {
22        if (freq[i] > 0) {
23          row.push_back(i);
24          freq[i]--;
25          exist = exist or freq[i] > 0;
26        }
27      }
28
29      ret.push_back(row);
30    }
31
32    return ret;
33  }
34};
35