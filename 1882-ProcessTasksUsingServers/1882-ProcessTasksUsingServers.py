# Last updated: 11/7/2026, 6:25:23 PM
1class Solution:
2    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
3        server_heap = [(s, i) for i, s in enumerate(servers)]
4        heapq.heapify(server_heap)
5        pending_heap = []
6
7        ans = []
8        current_time = 0
9        for t, task in enumerate(tasks):
10            if len(server_heap) == 0:
11                current_time = pending_heap[0][0]
12
13            while pending_heap and pending_heap[0][0] <= current_time:
14                _, server_index = heapq.heappop(pending_heap)
15                heapq.heappush(server_heap, (servers[server_index], server_index))
16
17            _, server_index = heapq.heappop(server_heap)
18            # print(t, task, 'current time:', current_time, 'server index:', server_index)
19            heapq.heappush(pending_heap, (current_time + task, server_index))
20            ans.append(server_index)
21            if t == current_time: current_time += 1
22
23        return ans