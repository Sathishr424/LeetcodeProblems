// Last updated: 20/10/2025, 5:55:15 pm
class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int ans = 0;
        for (String op: operations) {
            if (op.charAt(1) == '+') {
                ans += 1;
            } else {
                ans -= 1;
            }
        }
        return ans;
    }
}