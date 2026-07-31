# Last updated: 7/31/2026, 1:31:47 PM
1class Solution:
2    def minimumPushes(self, word: str) -> int:
3        n = len(word)
4
5        freq = [0] * 26
6        for char in word:
7            freq[ord(char) - ord('a')] += 1
8        freq.sort(reverse=True)
9
10        ans = 0
11        for i, cnt in enumerate(freq):
12            ans += (i // 8 + 1) * cnt
13        return ans