// Last updated: 24/6/2025, 7:10:11 pm
class Solution {
public:
    int repeatedStringMatch(string a, string b) {
        const int n = a.length();
        const int m = b.length();

        std::vector<int> lps(m);
        int j = 0;
        for (unsigned int i=1; i<m; i++) {
            while (j > 0 and b[i] != b[j]) {
                j = lps[j-1];
            }
            if (b[i] == b[j]) {
                lps[i] = ++j;
            }
        }
        const int nn = n + n * ceil((float) m / n);
        j = 0;
        for (unsigned int i=0; i < nn; i++) {
            while (j > 0 and a[i % n] != b[j]) {
                j = lps[j-1];
            }
            if (a[i % n] == b[j]) {
                j++;
                if (j == m) return ceil((float) (i + 1) / n);
            }
        }

        return -1;
    }
};