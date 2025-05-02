# Last updated: 2/5/2025, 4:45:22 pm
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        m = len(workers)

        tasks.sort()
        workers.sort(reverse=True)

        left = 0
        right = n

        def isGood(mid):
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

            if isGood(mid):
                left = mid + 1
            else:
                right = mid
            
        return left