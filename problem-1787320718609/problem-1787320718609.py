# Last updated: 8/21/2026, 7:28:38 PM
1class Solution:
2    def maximumWidth(self, planks: list[int]) -> int:
3        planks.sort()
4        cnts = Counter(planks)
5
6        n = len(planks)
7        freq = defaultdict(set)
8
9        ans = 1
10        for i in range(n):
11            if i > 0 and planks[i] == planks[i-1]: continue
12            left = planks[i]
13            ans = max(ans, cnts[left])
14            for j in range(i+1, n):
15                if j > i + 1 and planks[j] == planks[j-1]: continue
16                right = planks[j]
17                freq[left + right].add((left, right))
18
19        # print(dict(freq))
20
21        for num in freq:
22            curr = cnts[num]
23            for l, r in freq[num]:
24                if l == r:
25                    curr += cnts[l] // 2
26                else:
27                    curr += min(cnts[l], cnts[r])
28            ans = max(ans, curr)
29
30        return ans