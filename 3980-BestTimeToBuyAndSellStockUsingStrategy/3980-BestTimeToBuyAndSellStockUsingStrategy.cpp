// Last updated: 12/25/2025, 7:09:35 PM
class Solution {
public:
    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
        int n = prices.size();
        vector<long long> prefix(n+1, 0);
        long long best = 0;
        for (int i=0; i<n; i++) {
            prefix[i + 1] = prefix[i] + prices[i];
            best += prices[i] * strategy[i];
        }

        int half = k / 2;
        long long left = 0;
        long long right = 0;
        for (int i=k; i<n; i++) {
            right += (strategy[i] * prices[i]);
        }

        for (int i=0; i<n-k; i++) {
            best = max(best, left + (prefix[i + k] - prefix[i + half]) + right);
            left += (strategy[i] * prices[i]);
            right -= (strategy[i + k] * prices[i + k]);
        }
        best = max(best, left + (prefix[n] - prefix[n - half]) + right);
        
        return best;
    }
};