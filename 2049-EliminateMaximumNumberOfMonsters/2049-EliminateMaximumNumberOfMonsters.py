# Last updated: 12/6/2025, 5:39:24 am
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        arr = []
        for i in range(n):
            arr.append(ceil(dist[i]/speed[i]))
        arr.sort()

        index = 1
        while index < n and arr[index] > index:
            index += 1
        return index