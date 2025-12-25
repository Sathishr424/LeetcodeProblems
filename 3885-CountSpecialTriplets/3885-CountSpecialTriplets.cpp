// Last updated: 12/25/2025, 7:11:10 PM
const int N = 2e5 + 1;
int left_freq[N];
int right_freq[N];
int mod = 1e9 + 7;

class Solution {
public:
    int specialTriplets(vector<int>& nums) {
        int n = nums.size();

        memset(left_freq, 0, sizeof(left_freq));
        memset(right_freq, 0, sizeof(right_freq));

        for (int num: nums) {
            right_freq[num]++;
        }

        int ans = 0;
        for (int num: nums) {
            right_freq[num]--;

            int need = num * 2;
            ans += (left_freq[need] * 1LL * right_freq[need]) % mod;
            ans %= mod;

            left_freq[num]++;
        }

        return ans;
    }
};