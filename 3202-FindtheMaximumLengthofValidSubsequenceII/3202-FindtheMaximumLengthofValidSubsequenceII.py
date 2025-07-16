# Last updated: 16/7/2025, 11:37:41 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def maximumLength(self, nums: List[int], k) -> int:
        n = len(nums)

        ret = 0
        for match in range(k):
            counter = defaultdict(int)
            for i in range(n):
                need = (k - (nums[i] % k) - match) % k

                counter[nums[i] % k] = max(1, counter[need] + 1)
                ret = max(counter[nums[i] % k], ret)
                
            # print(counter)
        
        return ret