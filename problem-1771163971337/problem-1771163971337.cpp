// Last updated: 2/15/2026, 7:29:31 PM
1#include <cstring>
2#include <iostream>
3#include <unordered_map>
4#include <vector>
5
6using namespace std;
7
8class Solution {
9public:
10  int firstUniqueFreq(vector<int> &nums) {
11    int n = nums.size();
12    unordered_map<int, int> freq;
13    
14    for (int& num: nums) {
15      freq[num] += 1;
16    }
17
18    unordered_map<int, int> uniqCnt;
19    for (auto& it: freq) {
20      uniqCnt[it.second]++;
21    }
22
23    for (int& num: nums) {
24      if (uniqCnt[freq[num]] == 1) return num;
25    }
26    return -1;
27  }
28};
29