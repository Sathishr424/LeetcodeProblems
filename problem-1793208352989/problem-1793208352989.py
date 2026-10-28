# Last updated: 10/28/2026, 10:55:52 PM
1N = 10**16
2indexes = [0]
3digits = [0]
4values = [0]
5k = 2
6ten = 100
7curr = 9
8while curr <= N:
9    indexes.append(curr)
10    digits.append(k - 1)
11    values.append(ten // 10 - 1)
12    curr += ten * k - ((ten // 10) * k)
13    ten *= 10
14    k += 1
15
16# print(indexes)
17# print(digits)
18# print(values)
19#
20# tot = 0
21# for num in range(10, 100):
22#     tot += len(str(num))
23#
24# print(tot)
25
26
27class Solution:
28    def kthDigit(self, k: int) -> int:
29        # 9 * 1 + 90 * 2 + 1000 * 3 + 10000 * 4 + 100000 * 5
30        #
31        if k < 10: return k
32
33        k -= 1
34        index = bisect_right(indexes, k) - 1
35        digit_len = digits[index + 1]
36        start_value = values[index]
37        start_index = indexes[index]
38
39        diff = k - start_index + 1
40
41        val = diff // digit_len
42        ten = math.ceil((start_value + val + 1) / 10)
43        # print(start_value + val + 1, ten)
44
45        d = val - (val % 10)
46        start_value += d
47        left = diff - (d * digit_len)
48        arr = [str(num) for num in range(start_value + 1, start_value + 11)]
49        if ten % 2 == 0: 
50            arr = arr[::-1]
51        arr = ''.join(arr)
52        # print(arr, val, d, left)
53        ans = arr[left - 1]
54
55        # print(index, ('index=', indexes[index], 'digit_len=', digit_len, 'start=',start_value), ('diff=',diff, 'val=',val, 'ans=',ans))
56        return int(ans)
57