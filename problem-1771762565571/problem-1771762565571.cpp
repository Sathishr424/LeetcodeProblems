// Last updated: 2/22/2026, 5:46:05 PM
1#include <iostream>
2#include <vector>
3using namespace std;
4
5class Solution {
6public:
7  string maximumXor(string s, string t) {
8    int n = t.length();
9
10    int one = 0;
11    int zero = 0;
12
13    for (char &c : t) {
14      if (c == '0')
15        zero += 1;
16      else
17        one += 1;
18    }
19
20    string ans = "";
21    for (int i=0; i<n; i++) {
22      char& c = s[i];
23      if (c == '0') {
24        if (one == 0) {
25          ans += '0';
26          zero--;
27        } else {
28          ans += '1';
29          one--;
30        }
31      } else {
32        if (zero == 0) {
33          ans += '0';
34          one--;
35        } else {
36          ans += '1';
37          zero--;
38        }
39      }
40    }
41
42    return ans;
43  }
44};
45