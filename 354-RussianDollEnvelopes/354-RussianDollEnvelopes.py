# Last updated: 12/6/2025, 5:50:12 am
class Solution:
    def binary_search(self, a, x, n):
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if a[mid] < x: lo = mid + 1
            else: hi = mid
        return lo

    def maxEnvelopes(self, env: List[List[int]]) -> int:
        env.sort(key=lambda x: [x[0], -x[1]])
        tmp = [env[0][1]]
        ret = 1
        for i in range(1, len(env)):
            j = self.binary_search(tmp, env[i][1], ret)
            if j == ret:
                tmp.append(env[i][1])
                ret += 1
            else: 
                tmp[j] = env[i][1]
        return ret

        