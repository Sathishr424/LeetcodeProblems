# Last updated: 23/4/2025, 8:21:08 am
cmax = lambda x, y : x if x > y else y
class Solution:
    def countLargestGroup(self, n: int) -> int:
        sizes = [0] * 37
        largest_size = 0

        for num in range(1, n+1):
            s = 0
            while num:
                s += num % 10
                num //= 10
            
            sizes[s] += 1
            largest_size = cmax(sizes[s], largest_size)

        ret = 0
        for size in sizes:
            ret += size == largest_size

        return ret