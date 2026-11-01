# Last updated: 11/1/2026, 8:05:36 PM
1class Solution:
2    def smallest_prime_factor(self, n: int) -> int:
3        if n < 2:
4            return n
5
6        if n % 2 == 0:
7            return 2
8
9        i = 3
10        while i * i <= n:
11            if n % i == 0:
12                return i
13            i += 2
14
15        return n
16
17    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
18        if value == 1: return -1
19        p = self.smallest_prime_factor(value)
20        orig_p = p
21        orig_value = value
22
23        if p == -1: return -1
24        left = index
25        if p % 2 == 1 and left > 1:
26            left -= 1
27            value -= p
28            p = 2
29
30        if p * index >= value: return -1
31        if index == n-1: return value
32         
33        p = orig_p
34        value = orig_value
35        
36        right = n - index - 1
37        if p % 2 == 1 and right > 1:
38            right -= 1
39            value += p
40            p = 2
41        # print("Final value:", value, (p, right))
42        return value + (p * right)