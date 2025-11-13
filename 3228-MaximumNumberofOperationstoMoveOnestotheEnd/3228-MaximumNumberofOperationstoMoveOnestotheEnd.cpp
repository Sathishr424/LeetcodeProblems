// Last updated: 13/11/2025, 5:59:25 am
class Solution {
public:
    int maxOperations(string s) {
        int n = s.length();
        int ans = 0;
        int i = n-1;
        while (i >= 0 && s[i] == '1') {
            i--;
        }
        bool first = true;
        int ones = 0;
        while (i >= 0) {
            if (s[i] == '1') {
                int add = 0;
                if (s[i + 1] == '0') add++;
                while (i >= 0 && s[i] == '1') {
                    ans+=ones + 1;
                    i--;
                }
                ones += add;
            }
            i--;
        }

        return ans;
    }
};