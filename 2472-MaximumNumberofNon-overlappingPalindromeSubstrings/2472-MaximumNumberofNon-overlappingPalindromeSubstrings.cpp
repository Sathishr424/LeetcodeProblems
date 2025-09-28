// Last updated: 29/9/2025, 3:23:45 am
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1000000007;
    static const int BASE = 27;
    static const int MAXN = 2005; // matches your 2001 in Python

    long long powers[MAXN];

    Solution() {
        powers[0] = 1;
        for (int i = 1; i < MAXN; i++) {
            powers[i] = (powers[i - 1] * BASE) % MOD;
        }
    }

    int getAlp(char c) {
        return c - 'a';
    }

    int maxPalindromes(string st, int k) {
        int n = st.size();

        // prefix hashes
        vector<long long> prefix(n + 1, 0);
        long long s = 0;
        for (int i = 0; i < n; i++) {
            s = (s * BASE + getAlp(st[i])) % MOD;
            prefix[i + 1] = s;
        }

        // suffix hashes
        vector<long long> suffix(n + 1, 0);
        s = 0;
        for (int i = n - 1; i >= 0; i--) {
            s = (s * BASE + getAlp(st[i])) % MOD;
            suffix[i] = s;
        }

        vector<int> dp(n + 1, 0);

        for (int index = 0; index <= n; index++) {
            if (index > 0) dp[index] = max(dp[index], dp[index - 1]);

            for (int i = index + k - 1; i < n; i++) {
                if (st[i] == st[index]) {
                    int window = i - index + 1;

                    long long left = (prefix[i + 1] - (prefix[index] * powers[window]) % MOD + MOD) % MOD;
                    long long right = (suffix[index] - (suffix[i + 1] * powers[window]) % MOD + MOD) % MOD;

                    if (left == right) {
                        dp[i + 1] = max(dp[i + 1], dp[index] + 1);
                    }
                }
            }
        }

        return dp[n];
    }
};
