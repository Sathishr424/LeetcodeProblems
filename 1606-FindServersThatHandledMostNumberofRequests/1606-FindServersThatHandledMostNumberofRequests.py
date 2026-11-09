# Last updated: 11/9/2026, 3:05:02 PM
1class Solution:
2    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
3        n = len(arrival)
4
5        available = SortedList([i for i in range(k * 2)])
6        server_finish_time = [0] * k
7        # (finish_time, server_index)
8        in_process = []
9        servers_used = [0] * n
10
11        for i, t in enumerate(arrival):
12            l = load[i]
13
14            while in_process and in_process[0][0] <= t:
15                ft, server_index = heapq.heappop(in_process)
16                if server_finish_time[server_index] != ft: continue
17                available.add(server_index)
18                available.add(server_index + k)
19
20            index = available.bisect_left(i % k)
21            if index == len(available): continue
22
23            server = available[index] % k
24            servers_used[server] += 1
25            available.discard(server)
26            available.discard(server + k)
27
28            server_finish_time[server] = t + l
29            heapq.heappush(in_process, (t + l, server))
30
31        res = []
32        max_used = max(servers_used)
33        for server in range(n):
34            if servers_used[server] == max_used:
35                res.append(server)
36
37        return res