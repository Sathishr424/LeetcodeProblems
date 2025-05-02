# Last updated: 2/5/2025, 5:06:00 pm
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        m = len(workers)

        tasks.sort()
        workers.sort()

        left = 0
        right = n

        def isGood(mid):
            p = pills
            sl = workers[-mid-1:]

            for i in range(mid+1):
                if not sl: return False
                task = tasks[mid-i]
                if sl[-1] < task:
                    if p == 0: return False
                    a = task-strength
                    index = bisect_left(sl, a)
                    if index == len(sl): return False
                    del sl[index]
                    p -= 1
                else:
                    sl.pop()
            
            return True

        while left < right:
            mid = (left+right) // 2

            if isGood(mid):
                left = mid + 1
            else:
                right = mid
            
        return left