# Last updated: 18/9/2025, 6:30:02 am
N = 10 ** 5 + 1
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.tasks_priority = [0] * N
        self.tasks_userId = [0] * N
        self.tasks = []

        for userId, taskId, priority in tasks:
            self.tasks_priority[taskId] = priority
            self.tasks_userId[taskId] = userId
            self.tasks.append((-priority, -taskId))
        
        heapq.heapify(self.tasks)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks_priority[taskId] = priority
        self.tasks_userId[taskId] = userId
        heapq.heappush(self.tasks, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.tasks_priority[taskId] = newPriority
        heapq.heappush(self.tasks, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        self.tasks_priority[taskId] = -1

    def execTop(self) -> int:
        while self.tasks and (self.tasks_priority[-self.tasks[0][1]] == -1 or self.tasks_priority[-self.tasks[0][1]] != -self.tasks[0][0]):
            heapq.heappop(self.tasks)
    
        if self.tasks:
            _, taskId = heapq.heappop(self.tasks)
            self.tasks_priority[-taskId] = -1
            return self.tasks_userId[-taskId]
        
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()