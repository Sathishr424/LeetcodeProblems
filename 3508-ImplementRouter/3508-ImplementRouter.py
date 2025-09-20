# Last updated: 20/9/2025, 10:25:32 am
class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.packets = deque([])
        self.there = {}
        self.dest = defaultdict(lambda: deque([]))

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.there:
            return False
        
        self.packets.append((source, destination, timestamp))
        self.there[(source, destination, timestamp)] = 1
        
        if len(self.packets) > self.limit:
            self.forwardPacket()

        self.dest[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if self.packets:
            source, destination, timestamp = self.packets.popleft()
            self.dest[destination].popleft()
            del self.there[(source, destination, timestamp)]
            return [source, destination, timestamp]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        d = self.dest[destination]
        left = bisect_left(d, startTime)
        right = bisect_right(d, endTime)

        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)