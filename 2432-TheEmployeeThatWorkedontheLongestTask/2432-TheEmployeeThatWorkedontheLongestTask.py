# Last updated: 25/9/2025, 12:16:06 am
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev = 0
        best = 0
        e = 0
        for id, time in logs:
            task = time - prev
            if task > best or (task == best and id < e):
                best = task
                e = id
            prev = time

        return e
