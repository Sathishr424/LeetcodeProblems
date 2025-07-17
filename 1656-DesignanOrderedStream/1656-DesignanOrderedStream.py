# Last updated: 17/7/2025, 9:42:31 pm
class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.arr = [''] * n
        self.used = [0] * n
        self.output = [0] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.used[idKey] = 1
        self.arr[idKey] = value

        ret = []

        for i in range(idKey):
            if self.used[i] == 0: return []
        
        for i in range(idKey, self.n):
            if self.used[i] == 0 or self.output[i]: break
            ret.append(self.arr[i])
            self.output[i] = 1
        
        return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)