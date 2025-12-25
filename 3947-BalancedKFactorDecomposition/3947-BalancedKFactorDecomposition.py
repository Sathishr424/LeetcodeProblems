# Last updated: 12/25/2025, 7:10:27 PM
class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        # n = 10**5
        # k = 5
        can = []
        for i in range(1, n):
            if n % i == 0:
                can.append(i)

        ret = []
        min_diff = inf
        def rec(index, tot, rem, arr):
            nonlocal min_diff, ret
            if rem == 0:
                if tot == n:
                    diff = max(arr) - min(arr)
                    if diff < min_diff:
                        ret = arr[:]
                        min_diff = diff
                return

            for i in range(index, len(can)):
                if tot * can[i] <= n:
                    arr.append(can[i])
                    rec(i, tot * can[i], rem - 1, arr)
                    arr.pop()
                else:
                    return

        rec(0, 1, k, [])
        return ret

            