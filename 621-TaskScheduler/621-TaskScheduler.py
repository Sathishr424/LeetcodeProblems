# Last updated: 12/6/2025, 5:48:03 am
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = defaultdict(int)

        for t in tasks:
            tasks_count[t] += 1
    
        pending_tasks = []
        for task in tasks_count:
            pending_tasks.append(-tasks_count[task])

        heapq.heapify(pending_tasks)
        wait = 0
        stack = deque([])

        while pending_tasks or stack:
            if pending_tasks:
                cnt = -heapq.heappop(pending_tasks)
            else:
                cnt, time = stack.popleft()
                wait += time - wait
            
            cnt -= 1
            wait += 1

            if cnt > 0: stack.append((cnt, wait+n))

            if stack and stack[0][1] <= wait:
                heapq.heappush(pending_tasks, -stack.popleft()[0])
            
        return wait

