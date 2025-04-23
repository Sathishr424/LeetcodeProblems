# Last updated: 23/4/2025, 8:14:26 am
class Solution:
    def countLargestGroup(self, n: int) -> int:
        m = str(n)
        sizes = [0] * (min(10**4, int('9' * len(m))) + 1)
        largest_size = 0

        for num in range(1, n+1):
            s = 0
            while num:
                s += num % 10
                num //= 10
            
            sizes[s] += 1
            largest_size = max(sizes[s], largest_size)

        ret = 0
        for size in sizes:
            ret += size == largest_size

        return ret