# Last updated: 12/6/2025, 5:38:17 am
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        hash = defaultdict(int)
        for x, y in roads:
            hash[x] += 1
            hash[y] += 1
        
        arr = []
        for key in hash:
            arr.append((key, hash[key]))
        
        arr.sort(key=lambda x: -x[1])

        hash = {}
        ret = 0
        for i in range(len(arr)):
            hash[arr[i][0]] = n-i
        
        for x, y in roads:
            ret += hash[x] + hash[y]
        return ret