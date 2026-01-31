// Last updated: 1/31/2026, 12:47:53 PM
1#include <iostream>
2#include <vector>
3
4using namespace std;
5
6class Solution {
7public:
8  char nextGreatestLetter(vector<char> &letters, char target) {
9    bool init = true;
10    char ans = '-';
11
12    for (char &c : letters) {
13      if (c > target) {
14        if (init) {
15          ans = c;
16          init = false;
17        } else if (c < ans)
18          ans = c;
19      }
20    }
21
22    if (not init)
23      return ans;
24    return letters[0];
25  }
26};
27