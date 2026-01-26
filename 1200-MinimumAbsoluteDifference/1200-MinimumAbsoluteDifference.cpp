// Last updated: 1/26/2026, 12:36:15 PM
1#include <algorithm>
2#include <climits>
3#include <iostream>
4#include <vector>
5
6using namespace std;
7
8class Solution {
9public:
10  vector<vector<int>> minimumAbsDifference(vector<int> &arr) {
11    int n = arr.size();
12
13    int minDiff = INT_MAX;
14    sort(arr.begin(), arr.end());
15
16    for (int i = 1; i < n; i++) {
17      minDiff = min(minDiff, abs(arr[i] - arr[i - 1]));
18    }
19
20    vector<vector<int>> ret;
21    for (int i = 1; i < n; i++) {
22      if (abs(arr[i] - arr[i - 1]) == minDiff) {
23        ret.push_back({arr[i - 1], arr[i]});
24      }
25    }
26
27    return ret;
28  }
29};
30