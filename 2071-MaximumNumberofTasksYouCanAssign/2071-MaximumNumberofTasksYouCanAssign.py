# Last updated: 1/5/2025, 11:59:22 pm
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
        workers.sort()

        # print(tasks, workers)

        # 5, 6, 8, 9 => tasks
        # 4, 6, 8, 9 => workers
        ret = 0

        left = 0
        right = n
        ret = 0

        while left < right:
            mid = (left+right) // 2

            curr = pills
            cnt = 0
            
            sl = SortedList(workers)
            for task in tasks[:mid+1][::-1]:
                index = sl.bisect_left(task)
                # print(task, index, sl)
                if index == len(sl):
                    if curr > 0:
                        index = sl.bisect_left(task-strength)
                        if index < len(sl):
                            curr -= 1
                            cnt += 1
                            sl.remove(sl[index])
                    # else: break
                else:
                    cnt += 1
                    sl.remove(sl[index])

            # print((left, mid, right), cnt)
            if cnt >= mid+1:
                left = mid + 1
            else:
                right = mid
            
            ret = max(ret, cnt)
            

        return ret


        
