# Last updated: 23/4/2025, 8:10:27 am
class Solution:
    def countLargestGroup(self, n: int) -> int:
        sizes = defaultdict(int)
        largest_size = 0

        for num in range(1, n+1):
            s = 0
            while num:
                s += num % 10
                num //= 10
            
            sizes[s] += 1
            if sizes[s] > sizes[largest_size]:
                largest_size = s

        ret = 0
        for num in sizes:
            ret += sizes[num] == sizes[largest_size]

        return ret