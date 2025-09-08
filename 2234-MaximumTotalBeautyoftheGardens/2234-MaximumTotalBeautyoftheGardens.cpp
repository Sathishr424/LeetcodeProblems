// Last updated: 9/9/2025, 1:10:25 am
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maximumBeauty(vector<int>& flowers,
                            long long k,
                            long long target,
                            long long full,
                            long long partial) {
        int n = flowers.size();
        sort(flowers.begin(), flowers.end());

        // bisect_left equivalent
        int right = int(lower_bound(flowers.begin(), flowers.end(), target) - flowers.begin());
        int complete = n - right;

        vector<long long> prefix(n + 1, 0);
        long long need = 0;
        for (int i = n - 1; i >= 0; --i) {
            need += max(0LL, target - (long long)flowers[i]);
            prefix[i] = need;
        }

        vector<long long> partial_prefix(n, 0);
        long long cnt = 0;
        for (int i = 1; i < n; i++) {
            long long diff = (long long)flowers[i] - (long long)flowers[i - 1];
            cnt += diff * i;
            partial_prefix[i] = cnt;
        }

        auto isGood = [&](long long mid, long long rem, int c) -> bool {
            // bisect_left(flowers, mid, hi=n-c) - 1
            int index = int(lower_bound(flowers.begin(), flowers.begin() + (n - c), mid) - flowers.begin()) - 1;
            if (index < 0) return true;

            long long cntLocal = partial_prefix[index];
            long long diff = mid - (long long)flowers[index];

            return cntLocal + (long long)(index + 1) * diff <= rem;
        };

        long long max_ans = -1;
        for (int c = complete; c <= n; c++) {
            long long needToComplete = prefix[n - c];
            if (needToComplete > k) break;

            long long rem = k - needToComplete;

            long long l = 0, r = target - 1;
            if (c < n) {
                while (l < r) {
                    long long mid = (l + r + 1) / 2;

                    if (isGood(mid, rem, c)) {
                        l = mid;
                    } else {
                        r = mid - 1;
                    }
                }
            }

            long long curr = (long long)c * full + l * partial;
            max_ans = max(max_ans, curr);
        }

        return max_ans;
    }
};
