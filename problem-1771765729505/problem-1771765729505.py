# Last updated: 2/22/2026, 6:38:49 PM
1class Solution:
2    def countSequences(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4
5        freq = [defaultdict(int) for _ in range(n + 1)]
6
7        ans = 0
8        freq[0][1] = 1
9        for i in range(n):
10            num = nums[i]
11            for val in freq[i]:
12                cnt = freq[i][val]
13                freq[i+1][val * num] += cnt
14                freq[i+1][val] += cnt
15                freq[i+1][val / num] += cnt
16
17        for num in freq[n]:
18            if abs(num - k) > 0.00001: continue
19            ans += freq[n][num]
20
21        return ans