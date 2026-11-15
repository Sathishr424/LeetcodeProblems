// Last updated: 11/15/2026, 9:12:48 PM
1class Solution {
2public:
3    long long countConsistent(vector<int>& nums) {
4        int n = nums.size();
5        const int m = 20;
6        vector<array<int, 20>> prefix(1);
7        prefix[0].fill(0);
8        for (int num : nums) {
9            array<int, 20> newBits = prefix.back();
10            for (int b = 0; b < 20; b++) {
11                if (num & (1 << b)) {
12                    newBits[b] += 1;
13                }
14            }
15            prefix.push_back(newBits);
16        }
17
18        long long ans = 0;
19
20        auto getLeft = [&](int index) {
21            int l = 0;
22            int r = index;
23
24            while (l < r) {
25                int mid = (l + r) / 2;
26
27                int val = 0;
28                for (int b = 0; b < m; b++) {
29                    int bit = prefix[index + 1][b] - prefix[mid][b];
30                    if (bit == index - mid + 1) {
31                        val += 1 << b;
32                    }
33                }
34
35                if (val == nums[index]) {
36                    r = mid;
37                } else {
38                    l = mid + 1;
39                }
40            }
41
42            return l;
43        };
44
45        auto getRight = [&](int index) {
46            int l = index;
47            int r = n - 1;
48
49            while (l < r) {
50                int mid = (l + r + 1) / 2;
51
52                int val = 0;
53                for (int b = 0; b < m; b++) {
54                    int bit = prefix[mid + 1][b] - prefix[index][b];
55                    if (bit == mid - index + 1) {
56                        val += 1 << b;
57                    }
58                }
59
60                if (val == nums[index]) {
61                    l = mid;
62                } else {
63                    r = mid - 1;
64                }
65            }
66
67            return l;
68        };
69
70        int left = 0;
71        int right = -1;
72        unordered_map<int, int> prevs;
73        auto getPrev = [&](int key) {
74            auto it = prevs.find(key);
75            return it == prevs.end() ? -1 : it->second;
76        };
77
78        for (int i = 0; i < n; i++) {
79            left = getLeft(i);
80            right = getRight(i);
81
82            long long l = i - max(left, getPrev(nums[i]) + 1) + 1;
83            long long r = right - i + 1;
84            if (right > i) {
85                prevs[nums[i]] = i;
86            }
87            ans += l * r;
88        }
89
90        return ans;
91    }
92};