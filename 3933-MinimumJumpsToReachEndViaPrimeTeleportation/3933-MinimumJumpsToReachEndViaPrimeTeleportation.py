# Last updated: 12/25/2025, 7:10:36 PM
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
        
        max_num = max(nums)
        for num in primes:
            p_num = num
            while num <= max_num:
                if num in indexes:
                    for i in indexes[num]:
                        prime_indexes[p_num].append(i)
                num += p_num

        dis = [inf] * n
        heap = [(0, 0)]

        while heap:
            moves, index = heapq.heappop(heap)

            if dis[index] <= moves: continue
            dis[index] = moves
            if index == n-1: return moves

            moves += 1
            if index > 0 and dis[index - 1] > moves:
                heapq.heappush(heap, (moves, index - 1))
            if dis[index + 1] > moves:
                heapq.heappush(heap, (moves, index + 1))
            
            for i in prime_indexes[nums[index]]:
                if i == index or dis[i] <= moves: continue
                heapq.heappush(heap, (moves, i))
            
            prime_indexes[nums[index]] = []
        
        return n-1