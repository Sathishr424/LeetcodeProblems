# Last updated: 12/25/2025, 7:08:18 PM
class Solution:
    def maxPoints(self, t1: List[int], t2: List[int], k: int) -> int:
        n = len(t1)

        arr = []
        for i in range(n):
            arr.append((t1[i], i, 0))
            arr.append((t2[i], i, 1))

        arr.sort()

        used = [0] * n
        used_t1 = [0] * n
        tot = 0

        j = 0
        while j < n:
            num, i, a = arr.pop()
            if used[i]: continue

            used[i] = 1;
            tot += num

            if a == 0:
                used_t1[i] = 1
                k -= 1
            j += 1
        
        # print(tot, used_t1, k)
        heap = []
        for i in range(n):
            if used_t1[i]: continue
            heap.append(t1[i] - t2[i])
        # print(heap)
        heap.sort()
        while k > 0:
            num = heap.pop()
            # print(num)
            tot += num
            k -= 1

        return tot