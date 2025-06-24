// Last updated: 24/6/2025, 10:51:57 pm
#include <bits/stdc++.h>
using namespace std;

int cmin(int x, int y) { return x < y ? x : y; }
int cmax(int x, int y) { return x > y ? x : y; }
const int INF = 1e9;

vector<int> getKMP(const string& st) {
    int n = st.size();
    vector<int> lps(n);
    int j = 0;
    for (int i = 1; i < n; ++i) {
        while (j > 0 && st[i] != st[j]) {
            j = lps[j - 1];
        }
        if (st[i] == st[j]) {
            ++j;
            lps[i] = j;
        }
    }
    return lps;
}

class Solution {
public:
    int minValidStrings(vector<string>& words, string target) {
        int n = words.size();
        int m = target.size();

        vector<int> matches(m);

        for (const string& word : words) {
            vector<int> lps = getKMP(word);
            int j = 0;
            for (int i = 0; i < m; ++i) {
                while (j > 0 && target[i] != word[j]) {
                    j = lps[j - 1];
                }
                if (target[i] == word[j]) {
                    matches[i - j] = cmax(matches[i - j], j + 1);
                    ++j;
                    if (j == (int)word.size()) {
                        j = lps[j - 1];
                    }
                }
            }
        }

        vector<int> dp(m + 1, INF);
        dp[0] = 0;
        deque<int> dq;

        for (int i = 1; i <= m; ++i) {
            while (!dq.empty() && dq.front() < i) dq.pop_front();

            if (matches[i - 1]) {
                int index = i + matches[i - 1] - 1;
                if (index <= m) {
                    dp[index] = cmin(dp[index], dp[i - 1] + 1);

                    while (!dq.empty() && dq.back() < index && dp[dq.back()] > dp[index]) dq.pop_back();

                    if (dq.empty() || dq.back() < index) dq.push_back(index);
                }
            }

            if (!dq.empty()) {
                dp[i] = cmin(dp[i], dp[dq.front()]);
            }
        }

        return dp[m] == INF ? -1 : dp[m];
    }
};
