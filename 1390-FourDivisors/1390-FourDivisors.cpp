// Last updated: 1/4/2026, 6:54:12 AM
1const int N = 1e5 + 1;
2vector<int> primes;
3bool is_prime[N];
4
5struct Init {
6    Init() {
7        memset(is_prime, 1, sizeof(is_prime));
8        is_prime[0] = 0;
9        is_prime[1] = 0;
10
11        for (int i=2; i * i <= N; i++) {
12            if (is_prime[i]) {
13                for (int j=i*i; j<N; j+=i) is_prime[j] = 0;
14            }
15        }
16
17        for (int i=2; i<N; i++) {
18            if (is_prime[i]) primes.push_back(i);
19        }
20    }
21} initiate;
22
23long long calcPF(int num) {
24    if (is_prime[num]) return 0;
25    unordered_set<int> uniq;
26    uniq.insert(num);
27    uniq.insert(1);
28    
29    for (int p: primes) {
30        if (p * 1LL * p > num) {
31            if (is_prime[num]) uniq.insert(num);
32            break;
33        }
34        if (num % p == 0) {
35            uniq.insert(p);
36
37            while (num % p == 0) {
38                uniq.insert(num);
39                num /= p;
40            }
41
42            if (uniq.size() > 4) return 0;
43        }   
44    }
45
46    if (uniq.size() != 4) return 0;
47    long long sum = 0;
48    for (int num: uniq) sum += num;
49    return sum;
50}
51
52class Solution {
53public:
54    int sumFourDivisors(vector<int>& nums) {
55        long long ans = 0;
56        for (int num: nums) ans += calcPF(num);
57        return ans; 
58    }
59};