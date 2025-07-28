# Last updated: 28/7/2025, 8:42:28 pm
N = 10 ** 6 + 1
is_prime = [True] * N

is_prime[0] = False
is_prime[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if not is_prime[i]: continue
    for j in range(i * i, N, i):
        is_prime[j] = False

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        prime_indexes = defaultdict(list)
        primes = {}
        indexes = defaultdict(list)
        for i, num in enumerate(nums):
            indexes[num].append(i)
            if is_prime[num]:
                primes[num] = 1
        
        # print(list(primes.keys()))
        max_num = max(nums)
        for num in primes:
            p_num = num
            while num <= max_num:
                if num in indexes:
                    for i in indexes[num]:
                        prime_indexes[p_num].append(i)
                num += p_num
                # print(num)

        primes = list(primes.keys())
        # print(dict(prime_indexes))
    
        def check(index, moves):
            return visited[index] > moves

        dis = [inf] * n
        heap = [(0, 0)]

        while heap:
            moves, index = heapq.heappop(heap)

            if dis[index] <= moves: continue
            dis[index] = moves
            if index == n-1: continue

            moves += 1
            if index > 0 and dis[index - 1] > moves:
                heapq.heappush(heap, (moves, index - 1))
            if dis[index + 1] > moves:
                heapq.heappush(heap, (moves, index + 1))
            
            arr = prime_indexes[nums[index]]
            while arr:
                i = arr.pop()
                if i == index or dis[i] <= moves: continue
                heapq.heappush(heap, (moves, i))
        
        # print(dis)
        return dis[n-1]