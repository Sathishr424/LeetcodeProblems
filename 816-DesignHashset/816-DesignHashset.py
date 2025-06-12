# Last updated: 12/6/2025, 5:46:30 am
class MyHashSet:
    def __init__(self):
        self.arr = []
        self.bucket = 256
        for i in range(self.bucket+1):
            self.arr.append([])

    def add(self, key: int) -> None:
        if key <= self.bucket:
            for k in self.arr[key]:
                if k[0] == key: 
                    k[1] = 1
                    return
            
            self.arr[key].append([key, 1])
        else:
            tmp = key
            key %= 256

            for k in self.arr[key]:
                if k[0] == tmp:
                    k[1] = 1
                    return
            
            self.arr[key].append([tmp, 1])

    def remove(self, key: int) -> None:
        if key <= self.bucket:
            for k in self.arr[key]:
                if k[0] == key: 
                    k[1] = 0
                    return
        else:
            tmp = key
            key %= 256

            for k in self.arr[key]:
                if k[0] == tmp:
                    k[1] = 0
                    return

    def contains(self, key: int) -> bool:
        if key <= self.bucket:
            for k in self.arr[key]:
                if k[0] == key and k[1]: return True
        else:
            tmp = key
            key %= 256
            for k in self.arr[key]:
                if k[0] == tmp and k[1]: return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)