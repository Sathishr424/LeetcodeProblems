# Last updated: 16/4/2025, 3:13:12 pm
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pairs = defaultdict(int)
        total = 0

        stack = deque([])
        ret = 0
        good = 0

        for i in range(n):
            pairs[nums[i]] += 1
            total += pairs[nums[i]]-1
            stack.append(i)

            while stack and total >= k:
                ret += stack[0]+(n-i)-good
                good += 1
                
                num = nums[stack.popleft()]
                pairs[num] -= 1
                total -= pairs[num]
            
        return ret