# Last updated: 12/6/2025, 5:41:40 am
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hash = {}
        for x, y in paths:
            hash[x] = 1
        for _, y in paths:
            if y not in hash:
                return y
                