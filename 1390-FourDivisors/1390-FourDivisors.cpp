// Last updated: 1/4/2026, 6:43:49 AM
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
25    int o_num = num;
26    unordered_set<int> uniq;
27    uniq.insert(num);
28    uniq.insert(1);
29    
30    for (int p: primes) {
31        if (p * 1LL * p > num) {
32            if (is_prime[num]) uniq.insert(num);
33            break;
34        }
35        if (num % p == 0) {
36            uniq.insert(p);
37
38            while (num % p == 0) {
39                uniq.insert(num);
40                num /= p;
41            }
42
43            if (uniq.size() > 4) return 0;
44        }   
45    }
46
47    if (uniq.size() != 4) return 0;
48    long long sum = 0;
49    for (int num: uniq) sum += num;
50    return sum;
51}
52
53class Solution {
54public:
55    int sumFourDivisors(vector<int>& nums) {
56        long long ans = 0;
57        for (int num: nums) ans += calcPF(num);
58        return ans; 
59    }
60};