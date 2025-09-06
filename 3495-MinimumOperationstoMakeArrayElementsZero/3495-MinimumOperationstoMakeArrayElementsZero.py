# Last updated: 6/9/2025, 3:08:57 pm
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        N = 17
        powers = [0] * N

        for p in range(N):
            powers[p] = 4 ** p

        def process(arr):
            rem = 0
            op = 0
            index = 0
            while index < N and arr[index] == 0:
                index += 1
            for i in range(index, N):
                if arr[i] == 0: break
                op += min(arr[i], rem)
                rem = abs(arr[i] - rem)

            op += ceil(rem / 2)
            return op
        
        count = 0
        for l, r in queries:
            arr = [0] * N

            prev = l
            for p in range(1, N):
                if powers[p] <= l: continue
                arr[p] = (min(r + 1, powers[p]) - prev) * p
                prev = min(r + 1, powers[p])
                
                if powers[p] > r: break
            
            # print((l, r), arr)
            count += process(arr)
        
        return count