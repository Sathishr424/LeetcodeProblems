# Last updated: 3/10/2025, 11:02:54 pm
class Allocator:
    def __init__(self, n: int):
        self.memory = [0] * n
        self.n = n
        self.ids = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        free = 0
        for i in range(self.n):
            if self.memory[i] == 0:
                free += 1
                if free == size:
                    left = i - free + 1
                    for j in range(left, i + 1):
                        self.memory[j] = 1
                    self.ids[mID].append((left, i))
                    return left
            else:
                free = 0
        return -1

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for l, r in self.ids[mID]:
            for i in range(l, r + 1):
                self.memory[i] = 0
            freed += r - l + 1
        self.ids[mID] = []
        return freed

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)