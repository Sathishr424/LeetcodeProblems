// Last updated: 16/11/2025, 10:07:39 am
int mod = pow(10, 9) + 7;
class Solution {
public:
    int numSub(string s) {
        int n = s.length();
        long long ans = 0;
        int cnt = 0;
        for (int i=0; i<n; i++) {
            if (i > 0 && s[i] == s[i - 1]) {
                cnt += 1;
            } else {
                cnt = 1;
            }
            if (s[i] == '1') {
                ans += cnt;
                ans %= mod;
            }
        }
        return ans;
    }
};