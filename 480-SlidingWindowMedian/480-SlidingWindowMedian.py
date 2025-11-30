# Last updated: 1/12/2025, 2:06:54 am
1class Solution:
2    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
3        left = []
4        right = []
5        left_delete = defaultdict(int)
6        right_delete = defaultdict(int)
7        left_delete_cnt = 0
8        right_delete_cnt = 0
9        n = len(nums)
10        ret = []
11        
12        def remove_deleted():
13            nonlocal left_delete_cnt, right_delete_cnt
14            while left and left_delete[-left[0]]:
15                num = -heapq.heappop(left)
16                left_delete[num] -= 1
17                left_delete_cnt -= 1
18
19            while right and right_delete[right[0]]:
20                num = heapq.heappop(right)
21                right_delete[num] -= 1
22                right_delete_cnt -= 1
23
24        def adjust_left_right():
25            nonlocal left_delete_cnt, right_delete_cnt
26
27            left_cnt = len(left) - left_delete_cnt
28            right_cnt = len(right) - right_delete_cnt
29
30            ceil_half = ceil(k / 2)
31            half = k // 2
32
33            if left_cnt > ceil_half:
34                heapq.heappush(right, -heapq.heappop(left))
35            
36            if right_cnt > half:
37                heapq.heappush(left, -heapq.heappop(right))
38        
39        for i in range(k):
40            heapq.heappush(left, -nums[i])
41
42            if left and right and -left[0] > right[0]:
43                heapq.heappush(right, -heapq.heappop(left))
44
45            if len(left) > (i + 1 + 1) // 2:
46                heapq.heappush(right, -heapq.heappop(left))
47            
48            if len(right) > (i + 1) // 2:
49                heapq.heappush(left, -heapq.heappop(right))
50
51        if k % 2:
52            ret.append(-left[0])
53        else:
54            ret.append((-1 * left[0] + right[0]) / 2)
55
56        # print(left, right)
57
58        for i in range(k, n):
59            prev = nums[i - k]
60            if not right or prev < right[0]:
61                left_delete[prev] += 1
62                left_delete_cnt += 1
63            else:
64                right_delete[prev] += 1
65                right_delete_cnt += 1
66            
67            num = nums[i]
68            heapq.heappush(left, -num)
69            
70            remove_deleted()
71
72            if left and right and -left[0] > right[0]:
73                heapq.heappush(right, -heapq.heappop(left))
74            
75            remove_deleted()
76            
77            adjust_left_right()
78            
79            remove_deleted()
80
81            adjust_left_right()
82
83            if k % 2:
84                ret.append(-left[0])
85            else:
86                ret.append((-1 * left[0] + right[0]) / 2)
87            
88            # print(nums[i-k+1:i+1], "==", left, right, dict(left_delete), dict(right_delete), left_delete_cnt, right_delete_cnt)
89        return ret