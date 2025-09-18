# Last updated: 18/9/2025, 6:11:57 am
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.tasks_priority = {}
        self.tasks = []

        for userId, taskId, priority in tasks:
            self.tasks_priority[taskId] = [priority, userId]
            self.tasks.append((-priority, -taskId))
        
        heapq.heapify(self.tasks)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks_priority[taskId] = [priority, userId]
        heapq.heappush(self.tasks, (-priority, -taskId))
        # print(self.tasks_priority, 'add')

    def edit(self, taskId: int, newPriority: int) -> None:
        self.tasks_priority[taskId][0] = newPriority
        heapq.heappush(self.tasks, (-newPriority, -taskId))
        # print(self.tasks_priority, taskId, 'edit')

    def rmv(self, taskId: int) -> None:
        # print(self.tasks_priority, taskId, 'delete')
        del self.tasks_priority[taskId]

    def execTop(self) -> int:
        while self.tasks and (-self.tasks[0][1] not in self.tasks_priority or self.tasks_priority[-self.tasks[0][1]][0] != -self.tasks[0][0]):
            heapq.heappop(self.tasks)
        
        # print(self.tasks_priority, 'exec', self.tasks)

        if self.tasks:
            _, taskId = heapq.heappop(self.tasks)
            userId = self.tasks_priority[-taskId][1]
            del self.tasks_priority[-taskId]
            return userId
        
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()