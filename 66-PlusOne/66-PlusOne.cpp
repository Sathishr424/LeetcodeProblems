// Last updated: 1/1/2026, 12:29:04 PM
1class Solution {
2public:
3    vector<int> plusOne(vector<int>& digits) {
4        int n = digits.size();
5        int cnt = 0;
6        for (int i=n-1; i>=0; i--) {
7            if (digits[i] != 9) {
8                digits[i] += 1;
9                break;
10            }
11            digits[i] = 0;
12            cnt += 1;
13        }
14
15        if (cnt == n) {
16            digits.push_back(0);
17            for (int i=n-1; i>=0; i--) {
18                digits[i + 1] = digits[i];
19            }
20            digits[0] = 1;
21        }
22
23        return digits;
24    }
25};