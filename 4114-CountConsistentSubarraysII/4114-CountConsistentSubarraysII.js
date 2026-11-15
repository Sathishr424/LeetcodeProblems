// Last updated: 11/15/2026, 9:10:55 PM
1/**
2 * @param {number[]} nums
3 * @return {number}
4 */
5var countConsistent = function(nums) {
6    const n = nums.length;
7    const m = 20;
8    const prefix = [new Array(m).fill(0)];
9    for (const num of nums) {
10        const newBits = prefix[prefix.length - 1].slice();
11        for (let b = 0; b < 20; b++) {
12            if (num & (1 << b)) {
13                newBits[b] += 1;
14            }
15        }
16        prefix.push(newBits);
17    }
18
19    let ans = 0;
20
21    const getLeft = (index) => {
22        let l = 0;
23        let r = index;
24
25        while (l < r) {
26            const mid = Math.floor((l + r) / 2);
27
28            let val = 0;
29            for (let b = 0; b < m; b++) {
30                const bit = prefix[index + 1][b] - prefix[mid][b];
31                if (bit === index - mid + 1) {
32                    val += 1 << b;
33                }
34            }
35
36            if (val === nums[index]) {
37                r = mid;
38            } else {
39                l = mid + 1;
40            }
41        }
42
43        return l;
44    };
45
46    const getRight = (index) => {
47        let l = index;
48        let r = n - 1;
49
50        while (l < r) {
51            const mid = Math.floor((l + r + 1) / 2);
52
53            let val = 0;
54            for (let b = 0; b < m; b++) {
55                const bit = prefix[mid + 1][b] - prefix[index][b];
56                if (bit === mid - index + 1) {
57                    val += 1 << b;
58                }
59            }
60
61            if (val === nums[index]) {
62                l = mid;
63            } else {
64                r = mid - 1;
65            }
66        }
67
68        return l;
69    };
70
71    let left = 0;
72    let right = -1;
73    const prevs = new Map();
74    const getPrev = (key) => (prevs.has(key) ? prevs.get(key) : -1);
75
76    for (let i = 0; i < n; i++) {
77        left = getLeft(i);
78        right = getRight(i);
79
80        const l = i - Math.max(left, getPrev(nums[i]) + 1) + 1;
81        const r = right - i + 1;
82        if (right > i) {
83            prevs.set(nums[i], i);
84        }
85        ans += l * r;
86    }
87
88    return ans;
89};