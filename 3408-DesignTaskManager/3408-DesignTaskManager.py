# Last updated: 18/9/2025, 6:24:05 am
class Task:
    def __init__(self, priority, taskId):
        self.priority = priority
        self.taskId = taskId
    
    def __lt__(self, task):
        if self.priority == task.priority:
            return self.taskId > task.taskId
        
        return self.priority > task.priority

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.tasks_priority = {}
        self.tasks_userId = {}
        self.tasks = []

        for userId, taskId, priority in tasks:
            self.tasks_priority[taskId] = priority
            self.tasks_userId[taskId] = userId
            self.tasks.append(Task(priority, taskId))
        
        heapq.heapify(self.tasks)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks_priority[taskId] = priority
        self.tasks_userId[taskId] = userId
        heapq.heappush(self.tasks, Task(priority, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.tasks_priority[taskId] = newPriority
        heapq.heappush(self.tasks, Task(newPriority, taskId))

    def rmv(self, taskId: int) -> None:
        del self.tasks_priority[taskId]
        del self.tasks_userId[taskId]

    def execTop(self) -> int:
        while self.tasks and (self.tasks[0].taskId not in self.tasks_priority or self.tasks_priority[self.tasks[0].taskId] != self.tasks[0].priority):
            heapq.heappop(self.tasks)

        if self.tasks:
            task = heapq.heappop(self.tasks)
            userId = self.tasks_userId[task.taskId]
            del self.tasks_priority[task.taskId]
            del self.tasks_userId[task.taskId]
            return userId
        
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()