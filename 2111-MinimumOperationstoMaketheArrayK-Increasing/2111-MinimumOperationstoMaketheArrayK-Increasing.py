# Last updated: 15/8/2025, 11:00:03 pm
class Solution:
    def kIncreasing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0
        
        for i in range(k):
            stack = []
            cnt = 0
            for j in range(i, n, k):
                index = bisect_left(stack, nums[j] + 1)
                if index < len(stack):
                    stack[index] = nums[j]
                else:
                    stack.append(nums[j])
                cnt += 1
            ret += cnt - len(stack)

        return ret