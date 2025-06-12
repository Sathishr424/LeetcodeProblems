# Last updated: 12/6/2025, 5:40:32 am
class Solution:
    def minDeletions(self, st: str) -> int:
        new = defaultdict(int)
        for s in st: new[s] += 1
        cnt = 0
        hash = {}
        for k in sorted(list(new.values()), reverse=True):
            while k in hash and k > 0:
                cnt += 1
                k -= 1
            hash[k] = 1

        return cnt
