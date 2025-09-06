# Last updated: 6/9/2025, 3:10:31 pm
cmin = lambda x, y: x if x < y else y

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
                op += cmin(arr[i], rem)
                rem = abs(arr[i] - rem)

            return op + ceil(rem / 2)
        
        count = 0
        for l, r in queries:
            arr = [0] * N
            r += 1
            prev = l
            for p in range(1, N):
                if powers[p] <= l: continue
                arr[p] = (cmin(r, powers[p]) - prev) * p
                prev = cmin(r, powers[p])
                
                if powers[p] >= r: break
            
            count += process(arr)
        
        return count