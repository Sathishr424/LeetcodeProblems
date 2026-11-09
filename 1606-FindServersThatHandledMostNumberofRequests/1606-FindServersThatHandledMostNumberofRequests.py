# Last updated: 11/9/2026, 3:08:12 PM
1class Solution:
2    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
3        n = len(arrival)
4
5        available_servers = SortedList([i for i in range(k * 2)])
6        server_finish_time = [0] * k
7
8        # (finish_time, server_index)
9        in_process = []
10
11        servers_usage = [0] * k
12
13        for i, t in enumerate(arrival):
14            l = load[i]
15
16            while in_process and in_process[0][0] <= t:
17                finish_time, server_index = heapq.heappop(in_process)
18                if server_finish_time[server_index] != finish_time: continue
19                available_servers.add(server_index)
20                available_servers.add(server_index + k)
21
22            index = available_servers.bisect_left(i % k)
23            if index == len(available_servers): continue
24
25            server = available_servers[index] % k
26            servers_usage[server] += 1
27
28            available_servers.discard(server)
29            available_servers.discard(server + k)
30
31            server_finish_time[server] = t + l
32            heapq.heappush(in_process, (t + l, server))
33
34        max_used = max(servers_usage)
35        return [server for server in range(k) if servers_usage[server] == max_used]