# Last updated: 11/17/2026, 3:04:12 PM
1import math
2
3class Solution:
4    def minimumChanges(self, s: str, k: int) -> int:
5        n = len(s)
6        
7        # Step 1: Precompute valid divisors for each length up to n
8        divs = [[] for _ in range(n + 1)]
9        for d in range(1, n + 1):
10            # A valid divisor strictly less than L, so L starts at d * 2
11            for L in range(d * 2, n + 1, d):
12                divs[L].append(d)
13                
14        # Step 2: Precompute the minimum cost to make s[i:j] a semi-palindrome
15        cost = [[math.inf] * (n + 1) for _ in range(n + 1)]
16        
17        for i in range(n - 1):
18            for j in range(i + 2, n + 1):
19                length = j - i
20                min_changes = math.inf
21                
22                # Check all valid divisors for the current substring length
23                for d in divs[length]:
24                    curr_changes = 0
25                    
26                    # Each divisor divides the substring into 'd' groups
27                    for group in range(d):
28                        left = i + group
29                        right = j - d + group
30                        
31                        # Compare characters in the current group
32                        while left < right:
33                            if s[left] != s[right]:
34                                curr_changes += 1
35                            left += d
36                            right -= d
37                            
38                    if curr_changes < min_changes:
39                        min_changes = curr_changes
40                        
41                cost[i][j] = min_changes
42
43        # Step 3: Dynamic Programming to find minimum changes for k partitions
44        # dp[i][p] = min cost to partition first i characters into p substrings
45        dp = [[math.inf] * (k + 1) for _ in range(n + 1)]
46        dp[0][0] = 0
47        
48        for p in range(1, k + 1):
49            # i must be at least p * 2 because each substring needs length >= 2
50            for i in range(p * 2, n + 1):
51                min_val = math.inf
52                # j must leave at least (p - 1) * 2 characters for the first (p - 1) partitions
53                # and leave at least 2 characters for the current partition (j <= i - 2)
54                for j in range((p - 1) * 2, i - 1):
55                    if dp[j][p - 1] + cost[j][i] < min_val:
56                        min_val = dp[j][p - 1] + cost[j][i]
57                dp[i][p] = min_val
58                
59        return dp[n][k]