# Last updated: 30/11/2025, 12:40:35 am
1class Solution:
2    def beautifulSubarrays(self, nums: List[int]) -> int:
3        count = 0
4        bits = [0] * 32
5        freq = defaultdict(int)
6        freq[0] = 1
7        for j, num in enumerate(nums):
8            index = 0
9            while num:
10                bits[index] += num & 1
11                num >>= 1
12                index += 1
13
14            need = 0
15            for i in range(32):
16                if bits[i] % 2:
17                    need += 1 << i
18            count += freq[need]
19            freq[need] += 1
20            # print(j, bits, format(need, '032b'), count)
21    
22        return count
23            