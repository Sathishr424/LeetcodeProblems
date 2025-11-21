# Last updated: 22/11/2025, 3:09:04 am
class LRUCache:
    def __init__(self, capacity: int):
        self.time = 0
        self.capacity = capacity
        self.last_used = defaultdict(int)
        self.heap = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.last_used[key] = self.time
            heapq.heappush(self.heap, (self.time, key))
            self.time += 1
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.capacity:
            while self.heap and self.last_used[self.heap[0][1]] != self.heap[0][0]:
                heapq.heappop(self.heap)
            _, old_key = heapq.heappop(self.heap)
            del self.cache[old_key]
        
        self.cache[key] = value
        self.last_used[key] = self.time
        heapq.heappush(self.heap, (self.time, key))

        self.time += 1
        # print(self.heap, self.cache, dict(self.last_used))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)