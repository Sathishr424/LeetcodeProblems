# Last updated: 12/6/2025, 5:45:09 am
class RecentCounter:

    def __init__(self):
        self.arr = deque([])

    def ping(self, t: int) -> int:
        while self.arr and t - self.arr[0] > 3000:
            self.arr.popleft()
        self.arr.append(t)

        return len(self.arr)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)