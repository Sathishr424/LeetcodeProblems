# Last updated: 2/5/2025, 12:23:42 am
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        m = len(workers)

        """
        tasks = [10,15,30]
        workers = [0,10,10,10,10]
        p = 3
        s = 10
        """
        tasks.sort()
        workers.sort(reverse=True)

        # print(tasks, workers)

        # 5, 6, 8, 9 => tasks
        # 4, 6, 8, 9 => workers
        ret = 0

        left = 0
        right = n
        ret = 0

        def getCnt(mid):
            p = pills
            sl = SortedList(workers[:mid+1])

            for i in range(mid+1):
                if not sl: return False
                task = tasks[mid-i]
                if sl[-1] < task:
                    if p == 0: return False
                    index = sl.bisect_left(task-strength)
                    if index == len(sl): return False
                    p -= 1
                    sl.remove(sl[index])
                else:
                    sl.remove(sl[-1])
            
            return True

        while left < right:
            mid = (left+right) // 2

            if getCnt(mid):
                left = mid + 1
            else:
                right = mid
            
        return left


        
