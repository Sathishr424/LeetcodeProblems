# Last updated: 22/6/2025, 7:47:44 am
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ret = 0
        limit += 1
        for i in range(limit):
            for j in range(limit):
                for k in range(limit):
                    if i + j + k == n: ret += 1
        
        return ret