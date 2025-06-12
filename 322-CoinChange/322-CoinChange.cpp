// Last updated: 12/6/2025, 5:50:38 am
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        long dp[amount+1];
        for (int i = 1; i <= amount; ++i){
            dp[i] = INT_MAX-1;
        }
        dp[0] = 0;
        for (long i=0; i<=amount; i++){
            for (const long &coin: coins){
                if (i+coin <= amount){
                    dp[i+coin] = min(dp[i]+1, dp[i+coin]);
                }
            }
        }
        return dp[amount] == INT_MAX-1 ? -1 : dp[amount];
    }
};