// Last updated: 18/11/2025, 10:01:44 am
class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int n = bits.size();
        int i = 0;
        while (i < n-1) {
            if (bits[i] == 1) i++;
            i++;
        }
        if (i == n-1) return true;
        return false;
    }
};