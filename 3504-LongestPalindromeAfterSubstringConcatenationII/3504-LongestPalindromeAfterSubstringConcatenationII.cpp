// Last updated: 26/6/2025, 11:48:23 pm
#include <bits/stdc++.h>
using namespace std;

int cmax(int x, int y) {
    return x > y ? x : y;
}

class Solution {
public:
    int longestPalindrome(string s, string t) {
        int n = s.size();
        int m = t.size();
        int tot = n + m;
        string st = s + t;
        int ret = 1;

        function<int(int, int)> rec_left;
        function<int(int, int)> rec_right;
        function<int(int, int)> do_left;
        function<int(int, int)> do_right;

        rec_left = [&](int i, int j) -> int {
            if (i < 0 || j == tot) return 0;
            int ans = rec_left(i - 1, j);
            if (st[i] == st[j]) {
                int ii = i, jj = j;
                int cnt = 0;
                while (ii >= 0 && jj < tot && st[ii] == st[jj]) {
                    ii--;
                    jj++;
                    cnt += 2;
                }
                ans = cmax(ans, cnt);
            }
            return ans;
        };

        rec_right = [&](int i, int j) -> int {
            if (i < 0 || j == tot) return 0;
            int ans = rec_right(i, j + 1);
            if (st[i] == st[j]) {
                int ii = i, jj = j;
                int cnt = 0;
                while (ii >= 0 && jj < tot && st[ii] == st[jj]) {
                    ii--;
                    jj++;
                    cnt += 2;
                }
                ans = cmax(ans, cnt);
            }
            return ans;
        };

        do_left = [&](int left, int right) -> int {
            int cnt = rec_left(n - 1, right + 1);
            return right - left + cnt + 1;
        };

        do_right = [&](int left, int right) -> int {
            int cnt = rec_right(left - 1, n);
            return right - left + cnt + 1;
        };

        for (int i = 1; i < tot; ++i) {
            int left = i - 1;
            int right = i;
            while (left >= 0 && right < tot && st[left] == st[right]) {
                left--;
                right++;
            }
            left++;
            right--;
            ret = cmax(ret, right - left + 1);
            if (left >= n) ret = cmax(ret, do_left(left, right));
            if (right < n) ret = cmax(ret, do_right(left, right));

            left = i - 1;
            right = i + 1;
            while (left >= 0 && right < tot && st[left] == st[right]) {
                left--;
                right++;
            }
            left++;
            right--;
            ret = cmax(ret, right - left + 1);
            if (left >= n) ret = cmax(ret, do_left(left, right));
            if (right < n) ret = cmax(ret, do_right(left, right));
        }

        return ret;
    }
};
