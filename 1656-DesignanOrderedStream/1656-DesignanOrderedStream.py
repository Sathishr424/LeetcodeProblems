# Last updated: 17/7/2025, 9:43:26 pm
class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.arr = [''] * n
        self.used = [0] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.used[idKey] = 1
        self.arr[idKey] = value

        for i in range(idKey):
            if self.used[i] == 0: return []
        
        ret = []
        for i in range(idKey, self.n):
            if self.used[i] == 0: break
            ret.append(self.arr[i])
        
        return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)