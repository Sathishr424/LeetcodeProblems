# Last updated: 12/6/2025, 5:37:49 am
class LUPrefix:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.sizes = [0] * n
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        node1 = self.find(x)
        node2 = self.find(y)

        if node1 == node2: return 1

        if self.sizes[node2] > self.sizes[node1]:
            node2, node1 = node1, node2
        
        self.parents[node2] = node1
        self.sizes[node1] += self.sizes[node2]

    def upload(self, video: int) -> None:
        video -= 1

        self.sizes[video] = 1

        if video-1 >= 0 and self.sizes[video-1] != 0:
            self.union(video, video-1)
        
        if video+1 < len(self.parents) and self.sizes[video+1] != 0:
            self.union(video, video+1)

    def longest(self) -> int:
        return self.sizes[self.find(0)]

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()