# Last updated: 12/6/2025, 5:39:43 am
class SeatManager:

    def __init__(self, n: int):
        self.unreserved = []
        self.start = 1

    def reserve(self) -> int:
        if len(self.unreserved) == 0:
            self.unreserved.append(self.start)
            self.start += 1
        return heapq.heappop(self.unreserved)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)