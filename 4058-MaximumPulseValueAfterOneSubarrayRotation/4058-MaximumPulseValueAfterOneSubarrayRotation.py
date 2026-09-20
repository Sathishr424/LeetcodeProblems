# Last updated: 9/20/2026, 8:45:57 PM
1class Solution:
2    def maxValue(self, nums: List[int]) -> int:
3        n = len(nums)
4        alt_array = []
5        for i, num in enumerate(nums):
6            if i % 2:
7                alt_array.append(-num)
8            else:
9                alt_array.append(num)
10
11        inf = 10**20
12        @cache
13        def rec_odd(index, alt, odd, used):
14            if index == n:
15                if alt: return -inf
16                return 0
17
18            if not alt:
19                ans = rec_odd(index + 1, alt, odd, used) + alt_array[index]
20                if not used:
21                    ans = max(ans, rec_odd(index + 1, True, False, True) + alt_array[index])
22            else:
23                ans = rec_odd(index + 1, alt, not odd, used) + (-alt_array[index])
24                if odd:
25                    ans = max(ans, rec_odd(index + 1, False, odd, used) + (-alt_array[index]))
26
27            return ans
28
29        @cache
30        def rec_even(index, alt, even, used):
31            if index == n:
32                if alt: return -inf
33                return 0
34
35            if not alt:
36                ans = rec_even(index + 1, alt, even, used) + alt_array[index]
37                if not used:
38                    ans = max(ans, rec_even(index + 1, True, True, True) + (-alt_array[index]))
39            else:
40                ans = rec_even(index + 1, alt, not even, used) + (-alt_array[index])
41                if even:
42                    ans = max(ans, rec_even(index + 1, False, even, True) + (-alt_array[index]))
43
44            return ans
45
46        odd = rec_odd(0, False, False, False)
47        even = rec_even(0, False, False, False)
48        rec_odd.cache_clear()
49        rec_even.cache_clear()
50        # print(odd, even)
51
52        return max(odd, even)