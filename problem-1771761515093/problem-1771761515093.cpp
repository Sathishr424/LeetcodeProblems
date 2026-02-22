// Last updated: 2/22/2026, 5:28:35 PM
1#include <algorithm>
2#include <vector>
3#include <iostream>
4
5using namespace std;
6
7int fact[11];
8
9struct Init{
10  Init() {
11    fact[0] = 1;
12    fact[1] = 1;
13
14    for (int i=2; i<11; i++) fact[i] = fact[i-1] * i;
15  }
16} initiate;
17
18class Solution {
19public:
20  bool isDigitorialPermutation(int n) {
21    vector<int> a;
22    vector<int> b;
23    int num = n;
24
25    int sum = 0;
26    while (num) {
27      a.push_back(num % 10);
28      sum += fact[num % 10];
29      num /= 10;
30    }
31
32    while (sum) {
33      b.push_back(sum % 10);
34      sum /= 10;
35    }
36
37    sort(a.begin(), a.end());
38    sort(b.begin(), b.end());
39
40    if (a.size() != b.size()) return false;
41
42    for (int i=0; i<a.size(); i++) {
43      if (a[i] != b[i]) return false;
44    }
45
46    return true;
47  }
48};
49