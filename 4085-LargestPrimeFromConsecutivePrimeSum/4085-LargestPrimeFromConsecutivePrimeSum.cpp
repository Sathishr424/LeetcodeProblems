// Last updated: 12/25/2025, 7:08:21 PM
const int N = 1e6+1;
bool is_prime[N];
vector<int> primes;

struct Init {
    Init() {
        memset(is_prime, 1, sizeof(is_prime));
        is_prime[1] = 0;

        for (int i=2; i<=sqrt(N) + 1; i++) {
            if (!is_prime[i]) continue;
            for (int j=i*i; j<N; j+=i) {
                is_prime[j] = 0;
            }
        }

        for (int i=0; i<N; i++) {
            if (is_prime[i]) primes.push_back(i);
        }
    }
} init_instance;

class Solution {
public:
    int largestPrime(int n) {
        if (n <= 1) return 0;
        int sum = 0;
        int ans = 0;
        for (int prime: primes) {
            if (sum + prime > n) break;
            sum += prime;
            if (is_prime[sum]) ans = sum;
        }

        return ans;
    }
};