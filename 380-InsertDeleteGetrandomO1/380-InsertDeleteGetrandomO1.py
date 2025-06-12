# Last updated: 12/6/2025, 5:50:02 am
class RandomizedSet:
    def __init__(self):
        self.hash = {}
        self.elements = []
        self.deleted = []

    def insert(self, val: int) -> bool:
        if val in self.hash: return False
        if self.deleted:
            x = self.deleted.pop()
            self.hash[val] = x
            self.elements[x] = val
        else:
            self.hash[val] = len(self.elements)
            self.elements.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.hash:
            x = self.hash[val]
            index = len(self.elements) - len(self.deleted) - 1
            self.elements[x], self.elements[index] = self.elements[index], self.elements[x]
            self.hash[self.elements[x]] = x
            self.deleted.append(index)
            del self.hash[val]
            return True
        return False

    def getRandom(self) -> int:
        return self.elements[random.randrange(0, len(self.elements) - len(self.deleted))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()