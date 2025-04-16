# Last updated: 16/4/2025, 3:11:35 pm
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

            pairs[num] += 1
            total += pairs[num]-1
            stack.append(i)

            while stack and total >= k:
                left = stack[0]
                right = n-i
                ret += left+right-good
                good += 1
                num = nums[stack.popleft()]

                pairs[num] -= 1
                total -= pairs[num]
            
        return ret