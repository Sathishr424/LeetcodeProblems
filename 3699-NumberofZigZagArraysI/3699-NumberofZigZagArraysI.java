// Last updated: 28/9/2025, 7:17:41 pm
class Solution {
    public int zigZagArrays(int n, int l, int r) {
        int mod = 1000000007;

        int m = r - l + 1;
        int[][] dp = new int[m][2];

        long prefix = 0;
        long suffix = 0;

        for (int i = 0; i < m; i++) {
            if (i + 1 < m) {
                dp[i][1] = 1;
            }
            if (i > 0) {
                suffix += 1;
                dp[i][0] = 1;
            }
        }

        for (int i = 0; i < n - 1; i++) {
            long nextSuffix = 0;
            for (int j = 0; j < m; j++) {
                // subtract dp[j][0] from suffix
                suffix = (suffix - dp[j][0]) % mod;
                if (suffix < 0) suffix += mod;

                dp[j][0] = (int) prefix;
                nextSuffix = (nextSuffix + prefix) % mod;

                prefix = (prefix + dp[j][1]) % mod;
                dp[j][1] = (int) suffix;
            }
            suffix = nextSuffix;
            prefix = 0;
        }

        long ans = 0;
        for (int i = 0; i < m; i++) {
            ans = (ans + dp[i][0] + dp[i][1]) % mod;
        }

        return (int) ans;
    }
}
