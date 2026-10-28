# Last updated: 10/28/2026, 10:57:06 PM
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
16class Solution:
17    def kthDigit(self, k: int) -> int:
18        if k < 10: return k
19
20        k -= 1
21        index = bisect_right(indexes, k) - 1
22        digit_len = digits[index + 1]
23        start_value = values[index]
24        start_index = indexes[index]
25
26        diff = k - start_index + 1
27
28        val = diff // digit_len
29        ten = math.ceil((start_value + val + 1) / 10)
30
31        d = val - (val % 10)
32        start_value += d
33        left = diff - (d * digit_len)
34        arr = [str(num) for num in range(start_value + 1, start_value + 11)]
35        if ten % 2 == 0: 
36            arr = arr[::-1]
37        arr = ''.join(arr)
38        ans = arr[left - 1]
39        return int(ans)
40