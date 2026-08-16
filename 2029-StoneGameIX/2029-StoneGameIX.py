# Last updated: 8/17/2026, 4:33:53 AM
1class Solution:
2    def go(self, one, two, zero, curr):
3        alice = False
4        def substract(_one, _two, _zero):
5            nonlocal one, two, zero, curr
6            one -= _one
7            two -= _two
8            zero -= _zero
9            curr = (curr + _one + _two * 2) % 3
10
11
12        while True:
13            if curr == 1:
14                if one: substract(1, 0, 0)
15                elif zero: substract(0, 0, 1)
16                elif two: substract(0, 1, 0)
17                else: return False
18            elif curr == 2:
19                if two: substract(0, 1, 0)
20                elif zero: substract(0, 0, 1)
21                elif one: substract(1, 0, 0)
22                else: return False
23            else:
24                return alice
25
26            alice = not alice
27
28    def stoneGameIX(self, stones: List[int]) -> bool:
29        zero = 0
30        one = 0
31        two = 0
32
33        for stone in stones:
34            rem = stone % 3
35            if rem == 0:
36                zero += 1
37            elif rem == 1:
38                one += 1
39            else:
40                two += 1
41
42        curr = 0
43
44        if one and two:
45            return self.go(one - 1, two, zero, 1) or self.go(one, two - 1, zero, 2)
46        elif one:
47            return self.go(one - 1, two, zero, 1)
48        elif two:
49            return self.go(one, two - 1, zero, 2)
50        else:
51            return False