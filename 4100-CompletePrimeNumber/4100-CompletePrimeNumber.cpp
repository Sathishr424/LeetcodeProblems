// Last updated: 12/25/2025, 7:08:14 PM
class Solution {
public:
    bool isPrime(int num) {
        if (num == 1) return false;
        if (num == 2 || num == 3) return true;

        if (num % 2 == 0 || num % 3 == 0) return false;
        
        for (int i=5; i<=static_cast<int>(sqrt(num)); i+=2) {
            if (num % i == 0) return false;
        }
        return true;
    }
    
    bool completePrime(int num) {
        int r_num = num;
        int right = 0;
        int dig = 1;
        while (num) {
            int rem = num % 10;
            right = rem * dig + right;
            if (!isPrime(right) || !isPrime(r_num / dig)) return false;
            num /= 10;
            dig *= 10;
        }
        

        return true;
    }
};