// Last updated: 12/25/2025, 7:10:37 PM
class Solution {
public:
    bool isValid(string str) {
        for (char chr: str) {
            int a = chr;
            if (!((a >= (int)'a' && a <= (int)'z') || (a >= (int)'A' && a <= (int)'Z') || (a >= (int)'0' && a <= (int)'9') || a == 95)) {
                return false;
            }
        }
        return true;
    }

    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
        int n = code.size();
        vector<pair<string, string>> ret;
        unordered_set<string> valid_buisness = {"electronics", "grocery", "pharmacy", "restaurant"};
        for (int i=0; i<n; i++) {
            if (code[i].length() && isValid(code[i]) && valid_buisness.find(businessLine[i]) != valid_buisness.end() && isActive[i]) {
                ret.push_back({code[i], businessLine[i]});
            }
        }

        sort(ret.begin(), ret.end(), [](auto& a, auto& b) {
            return a.second < b.second || (a.second == b.second && a.first < b.first);
        });

        vector<string> res;
        for (auto& it: ret) res.push_back(it.first);

        return res;
    }
};