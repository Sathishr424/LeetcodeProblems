# Last updated: 16/4/2025, 3:09:41 pm
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pairs = defaultdict(int)
        total = 0

        stack = deque([])
        ret = 0
        good = 0

        for i in range(n):
            num = nums[i]

            total -= pairs[num] * (pairs[num]-1) // 2
            pairs[num] += 1
            total += pairs[num] * (pairs[num]-1) // 2
            stack.append(i)

            while stack and total >= k:
                left = stack[0]
                right = n-i
                ret += left+right-good
                good += 1
                num = nums[stack.popleft()]

                total -= pairs[num] * (pairs[num]-1) // 2
                pairs[num] -= 1
                total += pairs[num] * (pairs[num]-1) // 2
            
        return ret