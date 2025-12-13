// Last updated: 12/13/2025, 1:11:05 PM
1class Solution {
2public:
3    bool isValid(string str) {
4        for (char chr: str) {
5            int a = chr;
6            if (!((a >= (int)'a' && a <= (int)'z') || (a >= (int)'A' && a <= (int)'Z') || (a >= (int)'0' && a <= (int)'9') || a == 95)) {
7                return false;
8            }
9        }
10        return true;
11    }
12
13    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
14        int n = code.size();
15        vector<pair<string, string>> ret;
16        unordered_set<string> valid_buisness = {"electronics", "grocery", "pharmacy", "restaurant"};
17        for (int i=0; i<n; i++) {
18            if (code[i].length() && isValid(code[i]) && valid_buisness.find(businessLine[i]) != valid_buisness.end() && isActive[i]) {
19                ret.push_back({code[i], businessLine[i]});
20            }
21        }
22
23        sort(ret.begin(), ret.end(), [](auto& a, auto& b) {
24            return a.second < b.second || (a.second == b.second && a.first < b.first);
25        });
26
27        vector<string> res;
28        for (auto& it: ret) res.push_back(it.first);
29
30        return res;
31    }
32};