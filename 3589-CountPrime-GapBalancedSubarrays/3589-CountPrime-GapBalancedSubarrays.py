# Last updated: 21/6/2025, 11:36:03 pm
N = 10**4 * 5 + 1

is_prime = [1] * N
is_prime[1] = 0

for i in range(1, int(N ** 0.5) + 1):
    if not is_prime[i]: continue

    for j in range(i*i, N, i):
        is_prime[j] = 0

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        stack = deque([])
        ret = 0
        prev = 0
        cnts = defaultdict(int)
        sl = SortedList()

        for i in range(n):
            if is_prime[nums[i]]:
                while stack and abs(nums[i] - sl[0]) > k:
                    while cnts[sl[0]]:
                        cnts[stack.popleft()[0]] -= 1
                    sl.remove(sl[0])
                while stack and abs(nums[i] - sl[-1]) > k:
                    while cnts[sl[-1]]:
                        cnts[stack.popleft()[0]] -= 1
                    sl.remove(sl[-1])
                sl.add(nums[i])
                cnts[nums[i]] += 1
                stack.append((nums[i], prev, i))
                prev = i+1

            if len(stack) >= 2:
                ret += stack[-2][2] - stack[0][1] + 1

        return ret