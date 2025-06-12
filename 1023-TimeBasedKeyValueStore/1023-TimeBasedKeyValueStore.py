# Last updated: 12/6/2025, 5:44:44 am
class TimeMap:
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = {"hash": {}, "array": []}
        self.timemap[key]['hash'][timestamp] = value
        self.timemap[key]['array'].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap or len(self.timemap[key]['array']) == 0 or self.timemap[key]['array'][0][0] > timestamp: return ""
        if self.timemap[key]['array'][-1][0] < timestamp: return self.timemap[key]['array'][-1][1]
        i = timestamp

        while i > self.timemap[key]['array'][0][0]:
            if i in self.timemap[key]['hash']: return self.timemap[key]['hash'][i]
            i -= 1
        
        return self.timemap[key]['hash'][i]



# Your self.timemap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)