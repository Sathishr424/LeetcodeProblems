// Last updated: 15/8/2025, 2:15:14 pm
#include <bits/stdc++.h>
using namespace std;

const int base = 53;
const int mod = 1000000007;
vector<long long> powers(5000, 1);

class Solution {
public:
    int beautifulSplits(vector<int>& nums) {
        // nums.clear();
        // for (int i = 0; i < 5000; i++) {
        //     nums.push_back(rand() % 51);
        // }
        int n = nums.size();
        if (n < 3) return 0;

        vector<long long> prefix;
        prefix.push_back(0);
        long long s = 0;
        for (int num : nums) {
            s = s * base + (num + 1);
            s %= mod;
            prefix.push_back(s);
        }

        vector<array<int, 2>> visited(n, {n, n});

        function<int(int,int)> rec = [&](int left, int right) {
            int window = right - left + 1;
            if (n - right - 1 <= window) return 0;

            int ans = rec(left, right + 1);
            int l = right + 1;
            int r = l + window;

            long long left_s = prefix[right + 1] % mod;
            long long right_s = (prefix[r] - left_s * powers[window] % mod + mod) % mod;

            if (left_s != right_s) return ans;

            visited[l] = {r - 1, n - 1};
            ans += n - r;
            return ans;
        };

        function<int(int,int)> rec2 = [&](int left, int right) {
            int window = right - left + 1;
            if (n - right - 1 < window) return 0;

            int ans = rec2(left, right + 1);
            if (visited[left][0] <= right && visited[left][1] >= right) return ans;
            int l = right + 1;
            int r = l + window;

            long long left_s = (prefix[right + 1] - prefix[left] * powers[window] % mod + mod) % mod;
            long long right_s = (prefix[r] - prefix[right + 1] * powers[window] % mod + mod) % mod;

            if (left_s != right_s) return ans;

            return ans + 1;
        };

        int ret = rec(0, 0);
        for (int i = 1; i < n - 1; i++) {
            ret += rec2(i, i);
        }
        return ret;
    }
};

struct InitPowers {
    InitPowers() {
        for (int i = 1; i < 5000; i++) {
            powers[i] = powers[i - 1] * base % mod;
        }
    }
} initPowers;