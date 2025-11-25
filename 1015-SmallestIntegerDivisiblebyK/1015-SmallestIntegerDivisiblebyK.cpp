// Last updated: 25/11/2025, 7:48:59 am
class Solution {
public:
    int smallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) return -1;
        int rem = 1 % k;
        int n = 1;
        while (rem != 0) {
            rem = (rem * 10 + 1) % k;
            n++;
        }
        return n;
    }
};