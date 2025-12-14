// Last updated: 12/14/2025, 6:16:50 PM
1class Solution {
2public:
3    long long minMoves(vector<int>& balance) {
4        int n = balance.size();
5
6        long long pos = 0;
7        long long neg = 0;
8        for (int num: balance) {
9            if (num <= 0) pos += num;
10            else neg += -num;
11        }
12
13        if (neg > pos) return -1;
14
15        vector<int> left;
16        deque<int> right;
17        for (int i=0; i<n; i++) {
18            if (balance[i] > 0) {
19                left.push_back(i);
20            }
21        }
22
23        for (int i=0; i<n; i++) {
24            if (balance[i] > 0) {
25                right.push_back(i + n);
26            }
27        }
28        
29        for (int i=0; i<n; i++) {
30            if (balance[i] > 0) {
31                right.push_back(i + n * 2);
32            }
33        }
34        
35        long long op = 0;
36
37        for (int i=n; i<n+n; i++) {
38            int index = i % n;
39            while (balance[index] < 0) {
40                while (right.front() <= i) {
41                    right.pop_front();
42                }
43                int l_index = i - left.back();
44                int r_index = right.front() - i;
45
46                if (l_index < r_index) {
47                    int can = min(-balance[index], balance[left.back() % n]);
48                    balance[left.back() % n] -= can;
49                    balance[index] += can;
50                    op += can * 1LL * l_index;
51                    if (balance[left.back() % n] == 0) left.pop_back();
52                } else {
53                    int can = min(-balance[index], balance[right.front() % n]);
54                    balance[right.front() % n] -= can;
55                    balance[index] += can;
56                    op += can * 1LL * r_index;
57                    if (balance[right.front() % n] == 0) right.pop_front();
58                }
59            }
60            if (balance[index] > 0) {
61                left.push_back(i);
62            }
63        }
64
65        return op;
66    }
67};