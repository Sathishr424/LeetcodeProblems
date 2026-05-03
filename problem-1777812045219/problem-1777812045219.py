# Last updated: 5/3/2026, 6:10:45 PM
1class Solution:
2    def sortVowels(self, s: str) -> str:
3        n = len(s)
4        vowels = "aeiou"
5        freq = defaultdict(int)
6        first_index = {}
7
8        for i, char in enumerate(s):
9            if char in vowels:
10                freq[char] += 1
11                if char not in first_index: first_index[char] = i
12
13        arr = []
14        for char in first_index:
15            arr.append([freq[char], first_index[char], char])
16        if len(arr) == 0: return s
17
18        arr.sort(key=lambda x: (-x[0], x[1]))
19        index = 0
20        ans = list(s)
21        for i, char in enumerate(s):
22            if char in vowels:
23                ans[i] = arr[index][2]
24                arr[index][0] -= 1
25                if arr[index][0] == 0: index += 1
26
27        return ''.join(ans)