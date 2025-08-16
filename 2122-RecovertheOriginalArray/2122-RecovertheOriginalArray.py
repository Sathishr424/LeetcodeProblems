# Last updated: 16/8/2025, 1:52:46 pm
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        m = n // 2

        for i in range(1, n):
            k = nums[i] - nums[0]
            if k == 0: continue
            ret = []

            freq = defaultdict(int)
            for i in range(n):
                freq[nums[i]] += 1
            
            higher = []
            lower = []
            for i in range(n):
                if freq[nums[i]] == 0:
                    higher.append(nums[i])
                    continue
                freq[nums[i]] -= 1
                if freq[nums[i] + k]:
                    lower.append(nums[i])
                    freq[nums[i] + k] -= 1
                else:
                    higher.append(nums[i])
                    freq[nums[i]] += 1

            if len(lower) == m:
                ret = []
                new_k = (higher[0] - lower[0]) // 2
                # print(lower, higher, new_k)
                for i in range(m):
                    ret.append(lower[i] + new_k)
                    if lower[i] + new_k != higher[i] - new_k:
                        break
                else:
                    return ret

        return []
