# Last updated: 25/6/2025, 8:06:57 am
inf = float('inf')
mod = 10 ** 9 + 7
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prev = n-1
        comb = [0] * (n + 1)
        comb[n] = 1
        prefix = [0] * (n + 1)

        min_stack = deque([])
        max_stack = deque([])

        for i in range(n-1, -1, -1):
            while max_stack and max_stack[-1][0] < nums[i]:
                max_stack.pop()
            
            while min_stack and min_stack[-1][0] > nums[i]:
                min_stack.pop()
            
            max_stack.append((nums[i], i))
            min_stack.append((nums[i], i))

            while max_stack[0][0] - min_stack[0][0] > k:
                prev -= 1
                if max_stack[0][1] > prev:
                    max_stack.popleft()
                
                if min_stack[0][1] > prev:
                    min_stack.popleft()
            
            prefix[i] = (prefix[i+1] + comb[i + 1]) % mod

            comb[i] = (prefix[i] - prefix[prev + 1]) % mod

        return comb[0]