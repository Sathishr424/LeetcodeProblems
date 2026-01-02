// Last updated: 1/2/2026, 11:44:59 AM
1class Solution {
2public:
3    vector<int> plusOne(vector<int>& digits) {
4        int n = digits.size();
5        for (int i=n-1; i>=0; i--) {
6            if (digits[i] != 9) {
7                digits[i] += 1;
8                return digits;
9            }
10            digits[i] = 0;
11        }
12
13        digits.push_back(0);
14        for (int i=n-1; i>=0; i--) {
15            digits[i + 1] = digits[i];
16        }
17        digits[0] = 1;
18
19        return digits;
20    }
21};