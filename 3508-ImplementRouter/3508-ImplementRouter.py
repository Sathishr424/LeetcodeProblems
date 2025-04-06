# Last updated: 6/4/2025, 9:49:33 am
class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.hash = defaultdict(lambda: defaultdict(deque))
        self.packets = deque([])
        self.destToSource = defaultdict(dict)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if self.hash[source][destination] and self.hash[source][destination][-1] == timestamp: return False

        if len(self.packets) == self.limit:
            s, d = self.packets.popleft()
            self.hash[s][d].popleft()
        
        self.destToSource[destination][source] = 1
        
        self.hash[source][destination].append(timestamp)

        self.packets.append((source, destination))
        return True

    def forwardPacket(self) -> List[int]:
        if self.packets:
            s, d = self.packets.popleft()
            return [s, d, self.hash[s][d].popleft()]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        res = 0
        for source in self.destToSource[destination]:
            arr = self.hash[source][destination]
            start = bisect_left(arr, startTime)
            end = bisect_right(arr, endTime)
            
            res += end-start

        return res


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)