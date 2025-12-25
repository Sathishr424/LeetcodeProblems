// Last updated: 12/25/2025, 7:11:25 PM
class Solution {
public:
    int countPermutations(vector<int>& c) {
        int n = c.size();
        int mod = 1e9 + 7;

        int ans = 1;
        for (int i=1; i<n; i++) {
            if (c[i] <= c[0]) return 0;
            ans = ans * 1LL * (n - i) % mod;
        }

        return ans;    
    }
};