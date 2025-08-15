# Last updated: 15/8/2025, 10:59:28 pm
class Solution:
    def kIncreasing(self, nums: List[int], k: int) -> int:
        # N = 10 ** 5
        # nums = [random.randrange(N+1) for _ in range(N)]
        n = len(nums)
        ret = 0

        cnts = [0] * k
        for i in range(n):
            cnts[i % k] += 1
        
        for i in range(k):
            stack = []
            for j in range(i, n, k):
                index = bisect_left(stack, nums[j] + 1)
                if index < len(stack):
                    stack[index] = nums[j]
                else:
                    stack.append(nums[j])
            ret += cnts[i] - len(stack)

        return ret