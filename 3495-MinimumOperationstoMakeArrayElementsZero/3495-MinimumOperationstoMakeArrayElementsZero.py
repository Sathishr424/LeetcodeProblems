# Last updated: 15/6/2025, 7:54:23 pm
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        N = 15
        def process(arr):
            rem = 0
            cnt = 0
            for i in range(N, 0, -1):
                if arr[i] <= 0: continue
                num = arr[i]

                cnt += num // 2 * i
                if num % 2:
                    cnt += i
                    rem += i

            return cnt - (rem // 2)

        ret = 0
        for x, y in queries:
            num = x
            f = 0
            while num:
                num //= 4
                f += 1
            
            num = y
            to = 0
            while num:
                num //= 4
                to += 1
            
            prev = x
            arr = [0] * (N + 1)
            for power in range(f, to+1):
                curr = min(y + 1, 4 ** power)
                new_num = curr - prev
                prev = curr
                arr[power] = new_num

            ret += process(arr)

        return ret